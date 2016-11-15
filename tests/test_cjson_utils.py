
import json

from avogadro_plugin.utils import cjson_get_atoms, cjson_get_bonds

ethane_cjson = json.loads("""
{
    "chemical json": 0,
    "name": "ethane",
    "inchi": "1/C2H6/c1-2/h1-2H3",
    "formula": "C 2 H 6",
    "atoms": {
      "elements": {
        "number": [  1,   6,   1,   1,   6,   1,   1,   1 ]
      },
      "coords": {
        "3d": [  1.185080, -0.003838,  0.987524,
                 0.751621, -0.022441, -0.020839,
                 1.166929,  0.833015, -0.569312,
                 1.115519, -0.932892, -0.514525,
                -0.751587,  0.022496,  0.020891,
                -1.166882, -0.833372,  0.568699,
                -1.115691,  0.932608,  0.515082,
                -1.184988,  0.004424, -0.987522 ]
      }
    },
    "bonds": {
      "connections": {
        "index": [ 0, 1,
                   1, 2,
                   1, 3,
                   1, 4,
                   4, 5,
                   4, 6,
                   4, 7 ]
      },
      "order": [ 1, 1, 1, 1, 1, 1, 1 ]
    },
    "properties": {
      "molecular mass": 30.0690,
      "melting point": -172,
      "boiling point": -88
    }
}
""")

def test_ethane_atoms_properly_parsed():
    atoms = cjson_get_atoms(ethane_cjson)
    expected_atoms = [
        ( 1.185080, -0.003838,  0.987524, 1),
        ( 0.751621, -0.022441, -0.020839, 6),
        ( 1.166929,  0.833015, -0.569312, 1),
        ( 1.115519, -0.932892, -0.514525, 1),
        (-0.751587,  0.022496,  0.020891, 6),
        (-1.166882, -0.833372,  0.568699, 1),
        (-1.115691,  0.932608,  0.515082, 1),
        (-1.184988,  0.004424, -0.987522, 1)
    ]

    assert atoms == expected_atoms

def test_ethane_bonds_properly_parsed():
    bonds = cjson_get_bonds(ethane_cjson)
    expected_bonds = [{0, 1},
                      {1, 2},
                      {1, 3},
                      {1, 4},
                      {4, 5},
                      {4, 6},
                      {4, 7}]
    expected_bonds = { frozenset(s) for s in expected_bonds }
    bonds = { frozenset(s) for s in bonds }
    assert len(expected_bonds ^ bonds) == 0
