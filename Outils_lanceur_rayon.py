import numpy as np
import Object_rayon as oray

def intersection():
    # TODO fct calcul pts d'intersection entre un rayon et une surface
    pass

def reflexion():
    # TODO fct de reflexion
    pass

def refraction(P0, C0, O0, R, F, Fp, normal, n0, n1):
    """
    Calcul du rayon réfracté par la surface définie par F.

    :param P0: [X0, Y0, Z0], point d'origine du rayon lumineux incident
    :param C0: Vecteur [k0, l0, m0], vecteur unitaire de direction du rayon lumineux incident
    :param O0: [x0, y0, z0], origine du repère de la surface exprimé dans le repère de référence
    :param R: Matrice de rotation de passage du repère de référence au repère de la surface de réfraction
    :param F: Fonction algébrique du dioptre (F(x, y, z) = 0)
    :param Fp: Fp = (dF/dx)(P)*k + (dF/dy)(P)*l + (dF/dz)(P)*m
    :param normal: fonction giving le normal vector of the surface at point P = (x, y, z)
    :return: Pi0, Cp0
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
        sn = s - F(P)/Fp(P, C1)
        if np.abs(s - sn) < 1e-3:
            break
        s = sn

    # parametre du chemin origine -> intersection
    p = -P1[2]/C1[2] + sn
    # coordonnées de l'intersection
    Pi = P1 + C1*p
    # vecteur orthogonal a la surface F en Pi
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


def interaction(rayon, surface):
    """
    Refraction, reflexion  ou stop de rayon sur surface
    :param rayon:
    :param surface:
    :return: None
    """
    # TODO methode a tester
    if surface.interaction == "refraction":
        # refraction
        Pf0, Cp0 = refraction(rayon.origine, rayon.direction,
                              surface.origine, surface.R, surface.F, surface.Fp, surface.normal,
                              surface.materiaux[0].indice(rayon.longueur_onde),
                              surface.materiaux[1].indice(rayon.longueur_onde))
        # creation du rayon refacter et arret du rayon existant
        # TODO ne pas avoir systematiquement 1 comme surface d'arrive
        rayon.set_arrive(arrive=Pf0, nb_surface_arrive=1)
        oray.Rayon(Pf0, Cp0, rayon.chemin, rayon.champ, rayon.longueur_onde, rayon.surface_origine + 1)
    elif surface.interaction == "reflexion":
        pass
    elif surface.interaction == "stop":
        rayon.set_arrive(rayon.origine + 10 * rayon.direction, nb_surface_arrive=1)
    else:
        print("la surface : {} \n n'est pas de type connu".format(surface))
