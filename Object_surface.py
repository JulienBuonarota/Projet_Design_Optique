##
import ast
import numpy as np
import Outils_math as om

# class new-style defini avec C(object) -> dans python 3, c'est new style par defaut
class Sphere():
    def __init__(self, R=10, origine=(0, 0, 0), angles=(0, 0, 0)):
        """
        Dioptre sphérique
        :param R: rayon de la sphere. exp:
                  lumière de gauche à droite
                  Lentille biconvexe simple " () "
                  ( -> R<0
                  ) -> R>0
        :param origine: (x, y, z) dans le référenciel principal
        :param angles: (ax, ay, az) en radian
        """
        self.rayon = R
        self.origine = origine
        self.angles = angles

    def __repr__(self):
        return "Surface sphérique de Rayon = {}, Repère = {}, Angles = {}"\
            .format(self.rayon, self.origine, self.angles)

    def update_from_csv(self, dict_dioptre):
        for i in dict_dioptre.keys():
            dict_dioptre[i] = ast.literal_eval(dict_dioptre[i])
        self.__dict__.update(dict_dioptre)

S = Sphere(1)
# methode objet.__dic__ pour acceder a l'objet en tant que dict
# TODO inclure plusieur representation mathematique de la sphere (voir livre)

class Plan():
    # equation ax + by + cz + d = 0
    def __init__(self, coeff, origine=(0, 0, 0), angles=(0, 0, 0)):
        # coeff = (a, b, c, d)
        self.coeff = coeff
        self.origine = origine
        self.angles = angles
        self.R = om.matrice_rotation(*angles)


    def F(self, P):
        """
        Equation du plan
        ax + by + cz + d = F(P) = 0
        :param P:
        :return:
        """
        x, y, z = P
        a, b, c, d = self.coeff
        return a*x + b*y + c*z + d

    def Fp(self, P, C):
        """
        (dF/dx)(P)*k + (dF/dy)(P)*l + (dF/dz)(P)*m
        :param P:
        :param C:
        :return:
        """
        k, l, m = C
        a, b, c, d = self.coeff
        return a*k + b*l + c*m

    def normal(self, P):
        a, b, c, d = self.coeff
        return np.array((a, b, c))

    def coupe_x_0(self, hauteur):
        # coupe du plan de ymax = hauteur
        x0, y0, z0 = self.origine
        a, b, c, d = self.coeff
        z_1 = -1/c * (b*hauteur + d)
        z_2 = -1/c * (-b*hauteur + d)
        z = np.linspace(min(z_1, z_2), max(z_1, z_2), 100)
        y = -1/b*(c*z + d) + y0
        return z + z0, -1/b*(c*z + d) + y0







