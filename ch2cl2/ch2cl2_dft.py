"""Equilibrium properties of CH2Cl2, calculated using DFT/Orca"""

import numpy as np
from richmol.asymtop import atom_mass

# Ab initio calculations performed in Orca
#   geometry optimization: MP2/def2-TZVPP
#   dipole moment and polarizability: B3LYP/def2-TZVPP
#   electric field gradient: RKS+DKH2/DKH-def2-TZVP

atom_labels_35_35 = ["C", "H", "H", "Cl", "Cl"]
atom_labels_37_37 = ["C", "H", "H", "Cl37", "Cl37"]
atom_labels_35_37 = ["C", "H", "H", "Cl35", "Cl37"]

atom_masses_35_35 = [atom_mass(atom) for atom in atom_labels_35_35]
atom_masses_37_37 = [atom_mass(atom) for atom in atom_labels_37_37]
atom_masses_35_37 = [atom_mass(atom) for atom in atom_labels_35_37]

# Cartesian coordinates in Angstrom
atom_xyz = np.array(
    [
        [-0.00000000, -0.80142237, 0.00000072],
        [0.00000000, -1.41063135, -0.89396615],
        [0.00000000, -1.41062470, 0.89397212],
        [1.46614804, 0.17816692, -0.00000108],
        [-1.46614804, 0.17816692, -0.00000108],
    ]
)

# Molecular-frame dipole moment in au
dip_mol = [0.0, -0.6435, 0.0]

# Molecular-frame polarizability moment in au
pol_mol = [
    [48.4241, 0.0, 0.0],
    [0.0, 32.8223, 0.0],
    [0.0, 0.0, 27.4821],
]

# Molecular-frame EFG tensor on Cl1 in au**-3
efg_mol_cl1 = [
    [2.2769, 2.6482, 0.0],
    [2.6482, -0.1301, 0.0],
    [0.0, 0.0, -2.1468],
]

# Molecular-frame EFG tensor on Cl2 in au**-3
efg_mol_cl2 = [
    [2.2769, -2.6482, 0.0],
    [-2.6482, -0.1301, 0.0],
    [0.0, 0.0, -2.1468],
]
