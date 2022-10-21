from __future__ import annotations

from collections.abc import AsyncIterator, Iterator
from subprocess import Popen
from typing import List

import pytest

from chai import ChaiCmdExecutor, CheckingError, TypecheckingError
from chai.client import Source
from chai.cmd_executor import ParsingError


# Fixture to start and clean up Apalache's Shai server
#
# - `autouse=True`:
#
#   Ensures that the fixture is provided (i.e., that the server is started)
#   for every test.
#
# - `scope="module"`:
#
#   Specifies that this fixture is created only once for all tests in the module,
#   rather than created once per test. See
#   https://docs.pytest.org/en/6.2.x/fixture.html#scope-sharing-fixtures-across-classes-modules-packages-or-session
@pytest.fixture(autouse=True, scope="module")
def server() -> Iterator[Popen]:
    # TODO Pass port to server explicitly when that is supported
    process = Popen(["apalache-mc", "server"])
    yield process
    process.terminate()


# Fixture to provide and clean up a connected client for each test
#
# NOTE: In contrast to the `server` fixture, we do want to create this once for
# each test
@pytest.fixture
async def client(server: Popen) -> AsyncIterator[ChaiCmdExecutor]:
    # We need to ensure the server is created before we create the client
    _ = server
    async with ChaiCmdExecutor.create() as client:
        yield client


async def test_can_obtain_a_connection(client: ChaiCmdExecutor) -> None:
    assert client.is_connected()


async def test_can_check_model(client: ChaiCmdExecutor) -> None:
    spec = """
---- MODULE M ----
Init == TRUE
Next == TRUE
====
"""
    res = await client.check(spec)
    assert isinstance(res, dict)
    m = res["modules"][0]
    assert m["name"] == "M" and m["kind"] == "TlaModule"


async def test_can_check_model_with_aux_modules(client: ChaiCmdExecutor) -> None:
    spec = """
---- MODULE M ----
EXTENDS A
Next == TRUE
====
"""
    aux: List[Source.Input] = [
        """
---- MODULE A ----
Init == TRUE
====
"""
    ]
    res = await client.check(spec, aux)
    assert isinstance(res, dict)
    m = res["modules"][0]
    decls = m["declarations"]
    assert any(d["name"].startswith("Init") for d in decls)


async def test_checking_deadlocked_model_returns_deadlock_checking_error(
    client: ChaiCmdExecutor,
) -> None:
    spec = """
---- MODULE M ----
Init == TRUE
Next == FALSE
====
"""
    res = await client.check(spec)
    assert isinstance(res, CheckingError)
    assert res.checking_result == "Deadlock"


async def test_checking_invalid_model_returns_validation_checking_error(
    client: ChaiCmdExecutor,
) -> None:
    spec = r"""
---- MODULE M ----
VARIABLES
    \* @type: Bool;
    x,
    \* @type: Bool;
    y

Init == x = TRUE /\ y = TRUE
Next == x' = FALSE /\ y' = y
Inv == x
====
"""
    res = await client.check(spec, config={"checker": {"inv": ["Inv"]}})
    assert isinstance(res, CheckingError)
    assert res.checking_result == "Error"
    state1 = res.counter_example[0]["states"][1]
    assert state1 == {"#meta": {"index": 1}, "x": False, "y": True}


async def test_checking_model_with_type_errors_returns_type_error(
    client: ChaiCmdExecutor,
) -> None:
    spec = r"""
---- MODULE M ----
VARIABLES
    \* @type: Bool;
    x

Init == x = "foo"
Next == TRUE
====
"""
    res = await client.check(spec)
    print(res)
    assert isinstance(res, TypecheckingError)
    # Errors look something like:
    # [['M.tla:7:9-7:17', 'Arguments to = should have the same type. For arguments x, "foo" with types Bool, Str, in expression x = "foo"'], # noqa
    #  ['M.tla:7:1-7:17', 'Error when computing the type of Init']]
    assert len(res.errors) == 2


async def test_checking_model_with_invalid_syntax_returns_parsing_error(
    client: ChaiCmdExecutor,
) -> None:
    spec = r"""
---- MODULE M ----
Foo = x
====
"""
    res = await client.check(spec)
    assert isinstance(res, ParsingError)


async def test_typechecking_a_well_typed_model_succeeds(
    client: ChaiCmdExecutor,
) -> None:
    spec = r"""
---- MODULE M ----
EXTENDS Integers
VARIABLES
    \* @type: Int;
    x

Add1 == x + 1
====
"""
    res = await client.typecheck(spec)
    # We get a dictionary back
    assert isinstance(res, dict)
    # And the dictionary is an Apalache IR representation of the module
    assert res["name"] == "ApalacheIR"


async def test_typechecking_an_ill_typed_model_fails(
    client: ChaiCmdExecutor,
) -> None:
    spec = r"""
---- MODULE M ----
EXTENDS Integers
VARIABLES
    \* @type: Seq(Int);
    x

Add1 == x + 1
====
"""
    res = await client.typecheck(spec)
    assert isinstance(res, TypecheckingError)
    assert res.msg == "Encountered a typechecking error"
    assert res.errors == [
        [
            "M.tla:8:9-8:13",
            "An operator with the signature ((Int, Int) => Int) cannot be applied to the provided arguments of type Seq(Int) and Int",  # noqa: E501
        ],
        ["M.tla:8:1-8:13", "Error when computing the type of Add1"],
    ]


async def test_typechecking_a_syntacticall_invalid_model_is_a_parse_error(
    client: ChaiCmdExecutor,
) -> None:
    spec = r"""
---- MODULE M ----
Foo = "OOPS"
====
"""
    res = await client.typecheck(spec)
    assert isinstance(res, ParsingError)


async def test_parsing_a_valid_model_succeeds(
    client: ChaiCmdExecutor,
) -> None:
    spec = r"""
---- MODULE M ----
Foo == TRUE
====
"""
    res = await client.parse(spec)
    # We get a dictionary back
    assert isinstance(res, dict)
    # And the dictionary is an Apalache IR representation of the module
    assert res["name"] == "ApalacheIR"


async def test_parsing_an_invalid_model_fails(
    client: ChaiCmdExecutor,
) -> None:
    spec = r"""
---- MODULE M ----
Foo = "OOPS"
====
"""
    res = await client.parse(spec)
    assert isinstance(res, ParsingError)