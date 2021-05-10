##
import ast
import numpy as np
import Outils_math as om
import matplotlib.pyplot as plt
import Object_materiaux as oma

## Sphere
class Sphere():
    # list of editable elements of this class
    editable = ["rayon", "origine", "angles", "materiaux", "interaction"]
    
    def __init__(self, R=10, materiaux=[oma.AIR, oma.BK7], origine=(0, 0, 0), angles=(0, 0, 0), interaction="refraction"):
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
        self.R = om.matrice_rotation(*angles)
        # list de deux elements
        self.materiaux = materiaux
        self.interaction = interaction

    def __repr__(self):
        return "Surface sphérique de Rayon = {}, Repère = {}, Angles = {}"\
            .format(self.rayon, self.origine, self.angles)

    def repr_type(self):
        for key, value in self.__dict__.items():
            print("nom : {}, valeur : {}, type : {}"
                  .format(key, value, type(value)))

    def update_from_dict(self, dict_update):
        for i in self.__class__.editable:
            if i == "materiaux":
                l = []
                for m in ast.literal_eval(dict_update[i].strip()):
                    if m == 'AIR':
                        l.append(oma.AIR)
                    elif m == 'BK7':
                        l.append(oma.BK7)
                self.materiaux = l
            elif i == "interaction":
                self.__dict__[i] = dict_update[i].strip()
            elif i == "rayon":
                if isinstance(dict_update[i], np.float64):
                    self.__dict__[i] = dict_update[i]
                else:
                    self.__dict__[i] = ast.literal_eval(dict_update[i].strip())
            else:
                self.__dict__[i] = ast.literal_eval(dict_update[i].strip())

    def F(self, P):
        """
        Equation de la sphère
        x**2 + y**2 + (z - R)**2 - R**2
        :param P: point dans l'espace (x, y, z)
        :return: valeur numérique de F(x, y, z)
        """
        x, y, z = P
        return x**2 + y**2 + (z - self.rayon)**2 - self.rayon**2

    def Fp(self, P, C):
        """
        (dF/dx)(P)*k + (dF/dy)(P)*l + (dF/dz)(P)*m
        :param P: position dans l'espace (x, y, z)
        :param C: vecteur (k, l, m)
        :return:
        """
        k, l, m = C
        R = self.rayon
        x, y, z = P
        return 2*x*k + 2*y*l + 2*(z - R)*m

    def normal(self, P):
        R = self.rayon
        x, y, z = P
        return np.array([2*x, 2*y, 2*(z - R)])

    def represente(self):
        # Calcule un cercle à partir d'un rayon R, d'un repère (x0, y0, z0) et d'angles
        x0, y0, z0 = self.origine
        R = self.rayon
        z = np.linspace(0, 3, 150)

        if R > 0:
            yp = np.sqrt(R ** 2 - (z - R) ** 2)
            yn = -np.sqrt(R ** 2 - (z - R) ** 2)
        else:
            yp = np.sqrt(R ** 2 - (z + R) ** 2)
            yn = -np.sqrt(R ** 2 - (z + R) ** 2)

        # zd = z + z0
        ypd = yp + y0
        ynd = yn + y0

        ytot = np.concatenate((np.flip(ypd), ynd))
        if R < 0:
            ztot = np.concatenate((-np.flip(z), -z))
        else:
            ztot = np.concatenate((np.flip(z), z))
        return (ztot + z0, ytot)

    def get_dict(self):
        # TODO gerer les materiaux
        # return un dict composer des info editable de l'objet
        d = {}
        d["type_surface"] = "SPHERE"
        current_state = self.__dict__
        for i in self.__class__.editable:
            if i == "materiaux":
                d[i] = [m.nom for m in self.materiaux]
            else:
                d[i] = current_state[i]
        return d
                

## Plan
class Plan():
    # equation ax + by + cz + d = 0
    editable = ["coeff", "origine", "angles", "materiaux", "interaction"]
    def __init__(self, coeff=(1,1,1,1), materiaux=[oma.AIR, oma.BK7], origine=(0, 0, 0), angles=(0, 0, 0), interaction="refraction"):
        # coeff = (a, b, c, d)
        self.coeff = coeff
        self.origine = origine
        self.angles = angles
        self.R = om.matrice_rotation(*angles)
        self.materiaux = materiaux
        self.interaction = interaction

    def __repr__(self):
        return "Plan d'origine = {}".format(self.origine)

    def repr_type(self):
        for key, value in self.__dict__.items():
            print("nom : {}, valeur : {}, type : {}"
                  .format(key, value, type(value)))

    def F(self, P):
        """
        Equation du plan
        ax + by + cz + d = F(P) = 0
        :param P: point dans l'espace (x, y, z)
        :return: valeur numérique de F(x, y, z)
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

    def represente(self, hauteur=20):
        """
        coupe du plan de ymax = hauteur
        :param hauteur: hauteur de la coupe
        :return: z, y
        """
        x0, y0, z0 = self.origine
        a, b, c, d = self.coeff
        z_1 = -1/c * (b*hauteur + d)
        z_2 = -1/c * (-b*hauteur + d)
        z = np.linspace(min(z_1, z_2), max(z_1, z_2), 100)
        y = -1/b*(c*z + d) + y0
        return (z + z0, -1/b*(c*z + d) + y0)

    def get_dict(self):
        # return un dict composer des info editable de l'objet
        d = {}
        d["type_surface"] = "PLAN"
        current_state = self.__dict__
        for i in self.__class__.editable:
            if i == "materiaux":
                d[i] = [m.nom for m in self.materiaux]
            else:
                d[i] = current_state[i]
        return d

    def update_from_dict(self, dict_update):
        for i in self.__class__.editable:
            if i == "materiaux":
                l = []
                for m in ast.literal_eval(dict_update[i].strip()):
                    if m == 'AIR':
                        l.append(oma.AIR)
                    elif m == 'BK7':
                        l.append(oma.BK7)
            elif i == "interaction":
                self.__dict__[i] = dict_update[i].strip()
            else:
                self.__dict__[i] = ast.literal_eval(dict_update[i].strip())



# TODO fct represente qui regarde les rayons qui on traversé la surface
#  en déduire la partie du dioptre à plot
if __name__ == "__main__":
    S = Sphere(10, (0,0,5), (0,0,0))
    # z, y = S.represente()
    # plt.plot(z, y)
    print(S.__dict__)








