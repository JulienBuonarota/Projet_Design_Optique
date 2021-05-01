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

## rayon
P0 = np.array([0, 1, 0])
C0 = np.array([0, 1/np.sqrt(17), 4/np.sqrt(17)])
rayon_1 = oray.Rayon(P0, C0, 1, 1, 1, 0)
## Plan
O0 = np.array([0, 0, 0])
plan_1 = osur.Plan((0, 1, -1, 5), O0)
## SPhere
sphere_1 = osur.Sphere(R=50, origine=(0,0,20))
## Refraction
n0 = 1
n1 = 2

Pf0, Cp0 = olr.refraction(rayon_1.origine, rayon_1.direction,
                          O0, plan_1.R, plan_1.F, plan_1.Fp, plan_1.normal, n0, n1)

rayon_1.set_arrive(arrive=Pf0, nb_surface_arrive=1)
rayon_2 = oray.Rayon(Pf0, Cp0, 1, 1, 1, 1)

Pf1, Cp1 = olr.refraction(Pf0, Cp0, sphere_1.origine, sphere_1.R, sphere_1.F,
                          sphere_1.Fp, sphere_1.normal, n0, n1)

rayon_2.set_arrive(arrive=Pf1, nb_surface_arrive=2)
rayon_3 = oray.Rayon(Pf1, Cp1, 1, 1, 1, 2)
# pour pouvoir tracer le rayon
arrive = rayon_3.origine + 10*rayon_3.direction
rayon_3.set_arrive(arrive=arrive, nb_surface_arrive=3)
## Plot
# le dioptre
plt.plot(*plan_1.represente(20))
plt.plot(*sphere_1.represente())
plt.plot(*rayon_1.represente())
plt.plot(*rayon_2.represente())
plt.plot(*rayon_3.represente())



plt.grid()
plt.show()

##

