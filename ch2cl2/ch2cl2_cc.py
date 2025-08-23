"""Equilibrium properties of CH2Cl2, calculated using CC/CFOUR"""

import numpy as np
from richmol.asymtop import atom_mass
from scipy import constants

# Ab initio calculations performed in CFOUR
#   CCSD(T)/aug-cc-pVTZ

atom_labels_35_35 = ["C", "H", "H", "Cl", "Cl"]
atom_labels_37_37 = ["C", "H", "H", "Cl37", "Cl37"]
atom_labels_35_37 = ["C", "H", "H", "Cl35", "Cl37"]

atom_masses_35_35 = [atom_mass(atom) for atom in atom_labels_35_35]
atom_masses_37_37 = [atom_mass(atom) for atom in atom_labels_37_37]
atom_masses_35_37 = [atom_mass(atom) for atom in atom_labels_35_37]

# Cartesian coordinates in Angstrom
atom_xyz = (
    np.array(
        [
            [-0.00000000, 0.00000000, 1.53198123],
            [-1.69882181, 0.00000000, 2.67706854],
            [1.69882181, 0.00000000, 2.67706854],
            [0.00000000, -2.78847826, -0.34001413],
            [0.00000000, 2.78847826, -0.34001413],
        ]
    )
    * constants.value("Bohr radius")
    * 1e10
)

# Molecular-frame dipole moment in au
dip_mol = [0.0, 0.0, 0.6453958216]

# Molecular-frame EFG tensor on Cl1 in au**-3
efg_mol_cl1 = [
    [-1.9257953611, 0, 0],
    [0, 2.0398602604, 2.4812277132],
    [0, 2.4812277132, -0.1140648983],
]

# Molecular-frame EFG tensor on Cl2 in au**-3
efg_mol_cl2 = [
    [-1.9257953611, 0, 0],
    [0, 2.0398602604, -2.4812277132],
    [0, -2.4812277132, -0.1140648983],
]
