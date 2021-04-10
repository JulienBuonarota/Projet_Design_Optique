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

def Ray_tracing(R, P0, C0, O0):
    # Matrices de rotation
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

    ## Changement de repère du rayon
    #  coord de l'origine du rayon dans le repère d'origine
    X0 = 0
    Y0 = 1
    Z0 = 0
    #  coord normalise du vecteur de direction C0 = (k, l, m)
    k0 = 0
    l0 = 1/np.sqrt(17)
    m0 = 4/np.sqrt(17)
    #  origine du nouveau repère dans celui d'origine
    x0 = 0
    y0 = 0
    z0 = 20
    #  Calcul de l'origine et de la direction dans le nouveau repère
    P0 = np.array([X0, Y0, Z0])
    O0 = np.array([x0, y0, z0])
    C0 = np.array([k0, l0, m0])

    P1 = np.matmul(R, P0 - O0)
    C1 = np.matmul(R, C0)

    ## TODO II Find the point of intersection of the ray with the surface S.
    # calcul de l'intersection du rayon avec le plan z0 = 0 du nouveau repère
    # equation parametric du rayon sont : X = X1 + k1*s, Y = Y1 + l1*s, Z = Z1 + m1*s
    X1, Y1, Z1 = P1
    k1, l1, m1 = C1
    s0 = -Z1/m1
    X1s0 = X1 + k1*s0
    Y1s0 = Y1 + l1*s0

    # Dioptre = plan incline d'equation F(x1, y1, z1) = y1 - z1 + 5 (ici j'ignore x1, le rayon étant uniquement
    # dans le plan YZ
    def F(x, y, z):
        return y - z + 5
    Fp = l1 - m1

    # Calcul de l'intersection par algo de Newton-Raphson
    s = 0
    while True:
        x = X1s0 + k1*s
        y = Y1s0 + l1*s
        z = m1*s

        sn = s - F(x, y, z)/Fp
        if np.abs(s - sn) < 1e-3:
            break
        s = sn
    # parametre du chemin origine -> intersection
    p = s0 + sn
    # coordonnées de l'intersection
    Xf = X1 + k1*p
    Yf = Y1 + l1*p
    Zf = Z1 + m1*p
    Pf = np.array([Xf, Yf, Zf])
    # vecteur orthogonal a la surface F en Pf
    # TODO calcul de r en fonction des calculs précédent
    K = 0
    L = 1
    M = -1
    r = np.array([K, L, M])
    ## Find the change in direction of the ray refraction at surface S
    # indices de refraction
    n0 = 1
    n1 = 2

    # parametre de l'equation T**2 + 2aT + b = 0
    u = n0/n1
    a = u*(k1*K + l1*L + m1*M)/(K**2 + L**2 + M**2)
    b = (u**2 - 1)/(K**2 + L**2 + M**2)

    # Calcul de la solution de l'equation par algo de Newton-Raphson
    T = -b/(2*a)
    while True:
        Tn = (T**2 - b)/(2*(T + a))
        if np.abs(T - Tn) < 1e-3:
            break
        T = Tn

    # Unit direction vector of refracted ray
    Cp1 = u*C1 + T*r

    ## Transform the new ray-point coordinates and direction cosines
    #   back to the reference coordinates system
    Cp0 = np.matmul(R.T, Cp1)
    Pf0 = np.matmul(R.T, Pf) + O0




## Plot
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






