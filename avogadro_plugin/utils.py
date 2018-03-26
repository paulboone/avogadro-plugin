

def cjson_get_atoms(cjson):
    coords_json = cjson["atoms"]["coords"]["3d"]
    elements = cjson["atoms"]["elements"]["number"]

    coords = [ (*coords_json[i*3:(i+1)*3], elements[i]) for i in range(0, int(len(coords_json) / 3)) ]
    return coords

def cjson_get_bonds(cjson):
    bonds_json = cjson["bonds"]["connections"]["index"]

    bonds = [ (bonds_json[i*2:(i+1)*2]) for i in range(0, int(len(bonds_json) / 2)) ]
    return bonds
