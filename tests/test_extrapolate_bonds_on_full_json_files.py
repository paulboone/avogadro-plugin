import json
import pytest

from avogadro_plugin.utils import cjson_get_atoms, cjson_get_bonds, extrapolate_bonds


@pytest.mark.parametrize("cjson_file", [
    "tests/cjson/ethane.cjson",
    "tests/cjson/c540.cjson",
    "tests/cjson/cholesterol.cjson",
    "tests/cjson/tube-978.cjson",
])
def test_extrapolate_bonds_on_cjson_file(cjson_file):
    with open(cjson_file, "r") as f:
        cjson = json.load(f)

    atoms = cjson_get_atoms(cjson)
    bonds = cjson_get_bonds(cjson)

    bonds_ext = extrapolate_bonds(atoms)
    bonds_ext = { frozenset(s) for s in bonds_ext }
    bonds = { frozenset(s) for s in bonds }

    assert len(bonds ^ bonds_ext) == 0
