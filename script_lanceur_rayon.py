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

## Plot
# b = 10
# def F(P, C, b=10):
#     # P = (x, y, z)
#     return P[1] - b*P[2] + 5
# def Fp(P, C, b=10):
#     # P = (x, y, z)
#     # C = (k, l, m)
#     return C[1] - b*C[2]
# def normal(P, b=10):
#     return np.array([0, 1, -b])

# alpha = 0
# beta = 0
# gamma = 0
#
# Rgamma = np.array([[np.cos(gamma), -np.sin(gamma), 0],
#                    [np.sin(gamma), np.cos(gamma), 0],
#                    [0, 0, 1]]).reshape((3,3))
# Rbeta = np.array([[1, 0, 0],
#                    [0, np.cos(beta), -np.sin(beta)],
#                    [0, np.sin(beta), np.cos(beta)]]).reshape((3,3))
# Ralpha = np.array([[np.cos(alpha), 0, -np.sin(alpha)],
#                    [0, 1, 0],
#                    [np.sin(alpha), 0, np.cos(alpha)]]).reshape((3,3))
# R = np.matmul(Rgamma, np.matmul(Rbeta, Ralpha))

## rayon
P0 = np.array([0, 1, 0])
C0 = np.array([0, 1/np.sqrt(17), 4/np.sqrt(17)])
rayon_1 = oray.Rayon(P0, C0, 1, 1, 1, 0)
## Plan
O0 = np.array([0, 0, 0])
plan_1 = osur.Plan((0, 1, -1, 5), O0)
## SPhere
sphere_1 = osur.Sphere(R=100, origine=(0,0,20))
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

# # la rayon d'origine, de P0 à Pf0, ds la plan ZY
# a = (Pf0[1] - P0[1])/(Pf0[2] - P0[2])
# b = P0[1]
# z = np.linspace(P0[2], Pf0[2], 100)
# plt.plot(z, a*z + b)
#
# # la rayon refracte, de Pf0 dans la direction Cp0, ds la plan ZY
# z = np.linspace(Pf0[2], Pf0[2] + 20, 100)
# plt.plot(z, Cp0[1]/Cp0[2]*(z - Pf0[2]) + Pf0[1])
#
# # la rayon refracte, de Pf1 dans la direction Cp1, ds la plan ZY
# z = np.linspace(Pf1[2], Pf1[2] + 20, 100)
# plt.plot(z, Cp1[1]/Cp1[2]*(z - Pf1[2]) + Pf1[1])

#plt.ylim(-1, 6)

plt.grid()
plt.show()

##

