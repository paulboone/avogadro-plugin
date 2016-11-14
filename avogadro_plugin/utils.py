rcov = [0, 0.38, 0.32, 1.34, 0.90, 0.82, 0.77, 0.75, 0.73, 0.71, 0.69, 1.54, 1.30, 1.18, 1.11]



def extrapolate_bonds(atoms):
    bonds = []
    for i in range(0, len(atoms)):
        for j in range(i + 1, len(atoms)):
            distance = ((atoms[j][0] - atoms[i][0])**2 +
                        (atoms[j][1] - atoms[i][1])**2 +
                        (atoms[j][2] - atoms[i][2])**2 ) ** 0.5

            max_bond_distance = (rcov[atoms[i][3]] + rcov[atoms[j][3]] + 0.45)
            if distance >= 0.16 and distance <= max_bond_distance:
                bonds.append((i,j))

    return bonds
