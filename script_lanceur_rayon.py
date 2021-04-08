"""
Algorithme de lancement de rayon

input
les rayons (un rayon suffit, il permet d'accéder aux autres)
le systeme optique et ses caracteristiques

for dioptres in system.dioptre:
   for rayon_origine in rayon_pas_encore_calculé:
       rayon_refracté = calcul_rayon_refracté(rayon_origine, dioptre)
"""
## import
import numpy as np
# TODO implementation du script de lancement de rayon
# TODO lancer un rayon sur un surface plan
## TODO I tranform (Xb, Yb, Zb) and (kb, lb, mb) into their value
#    (X, Y, Z) and (k, l, m)
# Matrices de rotation
alpha = 2
beta = 2
gamma = 2

Rgamma = np.array([[np.cos(gamma), -np.sin(gamma), 0],
                   [np.sin(gamma), np.cos(gamma), 0],
                   [0, 0, 1]]).reshape((3,3))
Rbeta = np.array([[1, 0, 0],
                   [0, np.cos(beta), -np.sin(beta)],
                   [0, np.sin(beta), np.cos(beta)]]).reshape((3,3))
Ralpha = np.array([[np.cos(alpha), 0, -np.sin(alpha)],
                   [0, 1, 0],
                   [np.sin(alpha), 0, np.cos(alpha)]]).reshape((3,3))
R = np.matmul(Rgamma, np.matmul(Rbeta, Ralpha))

## TODO II Find the point of intersection of the ray with the surface S.

## TODO III Find the change in direction of the ray refraction,
#   reflection (or diffraction in the case of a grating) at the surface S.

## TODO IV Transform the new ray-point coordinates and direction cosines back to the (XYZ) system