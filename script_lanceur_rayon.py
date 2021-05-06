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
import matplotlib.pyplot as plt
import Object_surface as osur
import Object_rayon as oray
import Outils_lanceur_rayon as olr
import Object_system as osys
import Object_materiaux


## Plan
O0 = np.array([0, 0, 0])
plan_1 = osur.Plan(coeff=(0, 1, -1, 5), origine=O0)
## SPhere
sphere_1 = osur.Sphere(R=50, origine=(0,0,20))
sphere_2 = osur.Sphere(R=50, origine=(0,0,40), interaction="stop")
## rayon
R = oray.Rayon.creation_champ(10, 20, 0, 1, 500, 0, np.array((0,5,0)))
## Creation system
system = osys.system_optique("aaa", "()")
system.dioptres = [plan_1, sphere_1, sphere_2]
system.rayon = R
## propagation des rayons
system.propagation()
## Plot
system.plot()

##

