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

def Ray_tracing(P0, C0, O0, R, F, Fp, normal, n0, n1):
    """
    Calcul du rayon réfracté par la surface définie par F.

    :param P0: [X0, Y0, Z0], point d'origine du rayon lumineux incident
    :param C0: Vecteur [k0, l0, m0], vecteur unitaire de direction du rayon lumineux incident
    :param O0: [x0, y0, z0], origine du repère de la surface exprimé dans le repère de référence
    :param R: Matrice de rotation de passage du repère de référence au repère de la surface de réfraction
    :param normal: fonction giving le normal vector of the surface at point X
    :return:
    """
    ## Changement de repère du rayon
    #  Calcul de l'origine et de la direction dans le nouveau repère
    P1 = np.matmul(R, P0 - O0)
    C1 = np.matmul(R, C0)

    ## Find the point of intersection of the ray with the surface S.
    # calcul de l'intersection du rayon avec le plan z0 = 0 du nouveau repère
    # equation parametric du rayon sont : X = X1 + k1*s, Y = Y1 + l1*s, Z = Z1 + m1*s
    P1s0 = P1 - P1[2] / C1[2] * C1
    # Calcul de l'intersection par algo de Newton-Raphson
    s = 0
    while True:
        P = P1s0 + C1*s
        sn = s - F(P, C1)/Fp(P, C1)
        if np.abs(s - sn) < 1e-3:
            break
        s = sn

    # parametre du chemin origine -> intersection
    p = -P1[2]/C1[2] + sn
    # coordonnées de l'intersection
    Pi = P1 + C1*p
    # vecteur orthogonal a la surface F en Pf
    r = normal(Pi)

    ## Find the change in direction of the ray refraction at surface S
    # parametre de l'equation T**2 + 2aT + b = 0
    a = n0/n1 * np.sum(C1*r)/np.sum(r*r)
    b = ((n0/n1)**2 - 1)/np.sum(r*r)

    # Calcul de la solution de l'equation par algo de Newton-Raphson
    T = -b/(2*a)
    while True:
        Tn = (T**2 - b)/(2*(T + a))
        if np.abs(T - Tn) < 1e-3:
            break
        T = Tn

    # Unit direction vector of refracted ray
    Cp1 = n0/n1*C1 + T*r

    ## Transform the new ray-point coordinates and direction cosines
    #   back to the reference coordinates system
    Cp0 = np.matmul(R.T, Cp1)
    Pi0 = np.matmul(R.T, Pi) + O0
    return Pi0, Cp0




## Plot
def F(P, C):
    # P = (x, y, z)
    return P[1] - P[2] + 5
def Fp(P, C):
    # P = (x, y, z)
    # C = (k, l, m)
    return C[1] - C[2]
def normal(P):
    return np.array([0, 1, -1])

alpha = 0
beta = 0
gamma = 0

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

P0 = np.array([0, 1, 0])
C0 = np.array([0, 1/np.sqrt(17), 4/np.sqrt(17)])
O0 = np.array([0, 0, 20])

n0 = 1
n1 = 2

Pf0, Cp0 = Ray_tracing(P0, C0, O0, R, F, Fp, normal, n0, n1)
# le dioptre
z = np.linspace(0, 50, 100)
plt.plot(z, (z - 20) - 5)
# la rayon d'origine, de P0 à Pf0, ds la plan ZY
a = (Pf0[1] - P0[1])/(Pf0[2] - P0[2])
b = P0[1]
z = np.linspace(P0[2], Pf0[2], 100)
plt.plot(z, a*z + b)

# la rayon refracte, de Pf0 dans la direction Cp0, ds la plan ZY
z = np.linspace(Pf0[2], Pf0[2] + 20, 100)
plt.plot(z, Cp0[1]/Cp0[2]*(z - Pf0[2]) + Pf0[1])

#plt.ylim(-1, 6)

plt.grid()
plt.show()






