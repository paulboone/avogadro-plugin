
def extrapolate_bonds(atoms):
    bonds = []
    for i in range(0, len(atoms)):
        for j in range(i + 1, len(atoms)):
            distance = ((atoms[j][0] - atoms[i][0])**2 +
                        (atoms[j][1] - atoms[i][1])**2 +
                        (atoms[j][2] - atoms[i][2])**2 ) ** 0.5

            if distance >= 0.16:
                bonds.append((i,j))

    return bonds
