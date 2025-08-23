"""Equilibrium properties of S2Cl2, calculated using DFT/Orca"""

import numpy as np
from richmol.asymtop import atom_mass

# Ab initio calculations performed in Orca
#   geometry optimization: MP2/def2-TZVPP
#   dipole moment and polarizability: B3LYP/def2-TZVPP
#   electric field gradient: RKS+DKH2/DKH-def2-TZVP

atom_labels = ["S", "S", "Cl", "Cl"]
atom_labels_35_37 = ["S", "S", "Cl35", "Cl37"]

atom_masses = [atom_mass(atom) for atom in atom_labels]
atom_masses_35_37 = [atom_mass(atom) for atom in atom_labels_35_37]

# Cartesian coordinates in Angstrom
atom_xyz = np.array(
    [
        [0.62343451524828, 0.74851460771596, 0.74188708659932],
        [-0.62343451520743, -0.74851460764339, 0.74188708650493],
        [-0.00338636809538, 2.07205754892655, -0.69808708654412],
        [0.00338636805452, -2.07205754899912, -0.69808708656014],
    ]
)

# Molecular-frame dipole moment in au
dip_mol = [0.0000, 0.0000, 0.3647]

# Molecular-frame polarizability moment in au
pol_mol = [
    [44.5924, 6.6059, 0.0000],
    [6.6059, 93.6130, 0.000],
    [0.0000, 0.0000, 54.9267],
]

# Molecular-frame EFG tensor on Cl1 in au**-3
efg_mol_cl1 = [
    [-1.4841232, -1.0040039, 1.3800067],
    [-1.0040039, 0.6251046, -2.7506355],
    [1.3800067, -2.7506355, 0.8590186],
]

# Molecular-frame EFG tensor on Cl2 in au**-3
efg_mol_cl2 = [
    [-1.4841232, -1.0040039, -1.3800067],
    [-1.0040039, 0.6251046, 2.7506355],
    [-1.3800067, 2.7506355, 0.8590186],
]
