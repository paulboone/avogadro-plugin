
rcov = [0, 0.38, 0.32, 1.34, 0.90, 0.82, 0.77, 0.75, 0.73, 0.71, 0.69, 1.54, 1.30, 1.18, 1.11]


# From Pyykko doi: 10.1002/chem.200800987
rcov = [
  0.18, 0.32, 0.46,
  1.33, 1.02, 0.85, 0.75, 0.71, 0.63, 0.64, 0.67,
  1.55, 1.39, 1.26, 1.16, 1.11, 1.03, 0.99, 0.96,
  1.96,  1.71, 1.48,
  1.36, 1.34, 1.22, 1.19, 1.16, 1.11, 1.10, 1.12, 1.18,
  1.24, 1.21, 1.21, 1.16, 1.14, 1.17,
  2.10, 1.85,
  1.63, 1.54, 1.47, 1.38, 1.28, 1.25, 1.25, 1.20, 1.28, 1.36,
  1.42, 1.40, 1.40, 1.36, 1.33, 1.31,
  2.32, 1.96,
  1.80, 1.63, 1.76, 1.74, 1.73, 1.72, 1.68,
  1.69, 1.68, 1.67, 1.66, 1.65, 1.64, 1.70,
  1.62, 1.52, 1.46, 1.37, 1.31, 1.29, 1.22, 1.23, 1.24, 1.33,
  1.44, 1.44, 1.51, 1.45, 1.47, 1.42,
  2.23, 2.01,
  1.86, 1.75, 1.69, 1.70, 1.71, 1.72, 1.66,
  1.66, 1.68, 1.68, 1.65, 1.67, 1.73, 1.76,
  1.61, 1.57, 1.49, 1.43, 1.41, 1.34, 1.29, 1.28, 1.21, 1.22,
  1.36, 1.43, 1.62, 1.75, 1.65, 1.57
]


RADIUS_BUFFER = 0.45

def extrapolate_bonds(atoms):
    bonds = []

    atoms_z = list(enumerate(atoms))
    atoms_z = sorted(atoms_z, key=lambda x: x[1][2])

    max_rad = max([ rcov[a[1][3]] for a in atoms_z ])

    for i in range(0, len(atoms_z)):
        max_cutoff = rcov[atoms_z[i][1][3]] + max_rad + RADIUS_BUFFER
        for j in range(i + 1, len(atoms_z)):
            distance = ((atoms_z[j][1][0] - atoms_z[i][1][0])**2 +
                        (atoms_z[j][1][1] - atoms_z[i][1][1])**2 +
                        (atoms_z[j][1][2] - atoms_z[i][1][2])**2 ) ** 0.5

            if abs(atoms_z[j][1][2] - atoms_z[i][1][2]) > max_cutoff:
                break

            max_bond_distance = (rcov[atoms_z[i][1][3]] + rcov[atoms_z[j][1][3]] + RADIUS_BUFFER)
            if distance >= 0.16 and distance <= max_bond_distance:
                bonds.append((atoms_z[i][0],atoms_z[j][0]))

    return bonds


def cjson_get_atoms(cjson):
    coords_json = cjson["atoms"]["coords"]["3d"]
    elements = cjson["atoms"]["elements"]["number"]

    coords = [ (*coords_json[i*3:(i+1)*3], elements[i]) for i in range(0, int(len(coords_json) / 3)) ]
    return coords

def cjson_get_bonds(cjson):
    bonds_json = cjson["bonds"]["connections"]["index"]

    bonds = [ (bonds_json[i*2:(i+1)*2]) for i in range(0, int(len(bonds_json) / 2)) ]
    return bonds
