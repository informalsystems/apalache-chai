"""The Python implementation of the gRPC Shai client to Apalache."""

# Postpone evaluation of annotations
# see:
#  - https://stackoverflow.com/a/33533514/1187277
#  - https://peps.python.org/pep-0563/
from __future__ import annotations

from types import TracebackType
from typing import Optional, Type, TypeVar
import grpc
import transExplorer_pb2 as msg
import transExplorer_pb2_grpc as service


T = TypeVar("T")


class Chai:
    """Client for Human-Apalache Interaction

    This class imlements the contextmanager protocol, and is meant to bues be
    used in a with context in order to ensure resources are cleaned up.

    Example usage:

    ```
    with Chai() as chai:
        # TODO: Add key method invocations
        pass
    ```

    If you need to use the class outside of a `with` statement, be sure to
    obtain a connection before doing your work and to close the client when done:

    ```
    try:
      chai = Chai().connect()
      # Do stuff
    finally:
      chai.close()
    ```

    """

    def __init__(self, ip: str = "localhost", port: int = 8822) -> None:
        self._channel = grpc.insecure_channel(f"{ip}:{port}")
        self._conn: Optional[msg.Connection] = None
        try:
            self._stub = service.TransExplorerStub(self._channel)
        finally:
            self.close()

    def __enter__(self) -> None:
        self.connect()

    def __exit__(self, type: Type[T], value: T, traceback: TracebackType) -> None:
        # Unused variables
        _ = (type, value, traceback)
        self.close()

    def connect(self) -> Chai:
        """Obtain a connection from the server

        All other methods assume a connection has been obtained. This method is
        called automatically when the class is used as a context manager.
        """
        self._conn: Optional[msg.Connection] = self._stub.OpenConnection(
            msg.ConnectRequest()
        )
        return self

    def close(self) -> None:
        """Close the client, cleaning up connections and channels"""
        # TODO: Send RPC to terminate connection (just a courtesy for the server)
        self._channel.close()