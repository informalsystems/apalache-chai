import re
from pathlib import Path
from typing import List, Optional

from typing_extensions import Self

INSTANCE_LINE_PREFIX_RE = re.compile(r".*INSTANCE *")
EXTENDS_LINE_PREFIX_RE = re.compile(r" *EXTENDS *")

# Suffix for TLA files
TLA_SUFFIX = "tla"


def _get_comma_separated_deps(line: str) -> List[str]:
    """Find the dependencies from a line in a module"""
    # Drop the prefix parts of the lines
    rest = re.sub(EXTENDS_LINE_PREFIX_RE, "", re.sub(INSTANCE_LINE_PREFIX_RE, "", line))
    return [
        non_empty for non_empty in (dep.strip() for dep in rest.split(",")) if non_empty
    ]


def _get_dep_from_instance_line(line: str) -> List[str]:
    """Find the dependencies from an INSTANCE declaration"""
    rest = re.sub(INSTANCE_LINE_PREFIX_RE, "", line)
    # The dependency will be the first word in the line...
    dep = next(
        (d for d in rest.split(" ") if d),
        None,  # or, None if we don't have any words
    )
    if dep is None:
        return []
    else:
        return [dep]


def _get_module_deps(module: str) -> List[str]:
    """Extract the module dependencies from a TLA module

    For the grammar of TLA module imports, see

    - EXTENDS: https://github.com/tlaplus-community/tlaplus-standard/blob/3cbb0c251d63d5365f71aa0b3fea0719b6879edd/grammar/TLAPlus2Grammar.tla#L83 # noqa
    - INSTANCE: https://github.com/tlaplus-community/tlaplus-standard/blob/3cbb0c251d63d5365f71aa0b3fea0719b6879edd/grammar/TLAPlus2Grammar.tla#L141-L144 # noqa

    And for examples of both: http://lamport.azurewebsites.net/tla/newmodule.html#Section2
    """
    deps = []
    # Comma separated deps may extend over many lines
    in_comma_sep_deps = False
    for line in module.splitlines():
        if not in_comma_sep_deps and re.search(EXTENDS_LINE_PREFIX_RE, line):
            in_comma_sep_deps = True

        if not in_comma_sep_deps and re.search(INSTANCE_LINE_PREFIX_RE, line):
            if "," in line:
                in_comma_sep_deps = True
            else:
                new_deps = _get_dep_from_instance_line(line)
                deps.extend(new_deps)

        if in_comma_sep_deps:
            new_deps = _get_comma_separated_deps(line)
            # Check if we have a blank line,
            # in which case we don't add anything and keep searching
            if new_deps:
                deps.extend(new_deps)
                # If the line ends in a comma, we will have more deps to come
                if not line.rstrip().endswith(","):
                    in_comma_sep_deps = False

    return deps


def _load_deps_of_tla_file(tla_module: Path) -> List[str]:
    """Load all the found dependencies on disk for TLA+ module

    Return:
        a list of the contents of the dependenceis
    """
    content = tla_module.read_text()
    deps = _get_module_deps(content)
    return [
        dep
        for f in tla_module.parent.resolve().iterdir()
        if f.stem in deps and f.suffix.lstrip(".") == TLA_SUFFIX
        for dep in (_load_deps_of_tla_file(f) + [f.read_text()])
    ]


class Source:
    """
    In-memory representation of a TLA+ module and its dependencies.

    If you already have a TLA spec (and some support modules) loaded
    into a string, you can create a source like so:

    ```python
    source = Source(spec_str, aux=[support_module], format="tla")
    ```

    To initialize a `Source` from files on disk, use the class methods
    `of_file` or `of_file_load_deps`. E.g.,

    ```python
    source = Source.of_file_load_deps(Path("MySpec.tla"))
    ````
    """

    @classmethod
    def of_file(cls, p: Path, aux: List[Path]) -> Self:
        """Create a Source for use in an RPC

        Args:

        - `p`: The main file
        - `aux`: Any auxiliary files required as dependencies
        """
        return Source(
            source=p.read_text(),
            aux=[s.read_text() for s in aux],
            format=p.suffix.lstrip("."),  # last filename suffix, without leading "."
        )

    @classmethod
    def of_file_load_deps(cls, p: Path) -> Self:
        """Like `of_file` but it attempts to load dependencies from the file system

        Args:

        - `p`: The main file
        """
        if not (p.suffix.lstrip(".") == TLA_SUFFIX):
            raise ValueError(
                f"dependencies can only be loaded for TLA files, given: {p}"
            )
        # The directory in which the file is located
        source = p.read_text()
        aux = _load_deps_of_tla_file(p)
        return Source(source=source, aux=aux, format=TLA_SUFFIX)

    def __init__(
        self,
        source: str,
        *,  # force all other arguments to be keyword-only
        aux: Optional[List[str]] = None,
        format: str = "tla",
    ) -> None:
        """Create a source

        Args:

        - `source`: A string representing a TLA spec
        - `aux`: Auxiliary modules used as dependencies by the `source`
        - `format`: The format of the `source` (`"tla"` or `"json"`)
        """
        self.format: str = format
        self.spec: str = source
        self.aux: List[str] = aux or []

    def to_dict(self) -> dict:
        """A representation of the source in a dictionary that serializes into
        a format consistent with Apalache config inputs configurations.
        """
        return {
            "input": {
                "source": {
                    "type": "string",
                    "content": self.spec,
                    "aux": self.aux,
                    "format": self.format,
                }
            }
        }
