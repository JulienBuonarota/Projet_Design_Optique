
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

##
class Rayon():
    instances = []
    # nb de rayon a calculer
    nb_calcule = 0

    def __init__(self, origine, direction, chemin, champ, longueur_onde, nb_surface_refraction):
        self.origine = origine
        self.direction = direction
        self.chemin = chemin  # meme que le rayon incident
        self.champ = champ  # meme que le rayon incident
        self.longueur_onde = longueur_onde # meme que le rayon incident
        self.surface_origine = nb_surface_refraction
        # self.interaction = interaction
        self.calcule = False
        # list des instance
        self.__class__.instances.append(self)
        self.__class__.nb_calcule += 1

    def __repr__(self):
        try:
            return "rayon d'origine = {}, de direction {} et d'arrive = {}"\
                .format(self.origine, self.direction, self.arrive)
        except AttributeError:
            return "rayon d'origine = {}, de direction {}" \
                .format(self.origine, self.direction)

    def __eq__(self, other):
        b = (self.origine == other.origine)
        b += (self.direction == other.direction)
        b += (self.chemin == other.chemin)
        b += (self.champ == other.champ)
        b += (self.longueur_onde == other.longueur_onde)
        b += (self.surface_origine == other.surface_origine)
        b += (self.interaction == other.interaction)
        if b == 7:
            return True
        else:
            return False

    def set_arrive(self, arrive, nb_surface_arrive):
        self.arrive = arrive
        self.surface_arrive = nb_surface_arrive
        self.calcule = True
        self.__class__.nb_calcule -= 1

    def represente(self):
        # de depart a arrive, return z et y
        x0, y0, z0 = self.origine
        try:
            x1, y1, z1 = self.arrive
        except AttributeError:
            x1, y1, z1 = self.origine + 10 * self.direction
        a = (y1 - y0)/(z1 - z0)
        b = y0 - a*z0
        z = np.linspace(z0, z1, 100)
        return (z, a*z + b)

    def get_instances_df(self):
        df_rayon = pd.DataFrame()
        for i in self.__class__.instances:
            df_rayon = df_rayon.append(i.__dict__, ignore_index=True)
        return df_rayon

    @classmethod
    def creation_champ(self, nb_rayon, hauteur, angle, num_champ, longueur_onde, nb_surface_refraction=0, origine_surface=(0,0,0)):
        """
        :param angle: en radian
        """
        x0, y0, z0 = origine_surface
        # plan ZY -> k=0
        k, l, m = 0, np.sin(angle), np.cos(angle)
        C = np.array((k, l, m))
        # creation des rayons
        for count, h in enumerate(np.linspace(-hauteur/2, hauteur/2, nb_rayon)):
            # point d origine ds le repere de la surface
            P = np.array((0, h, 0)) + origine_surface
            # origine en avant de cette surface
            P = P - 10*C
            # Creation du rayon de meme num de champ mais de chemin different
            r = Rayon(P, C, count, num_champ, longueur_onde, nb_surface_refraction)
        return r

##
if __name__ == "__main__":
    R = Rayon((0,0,0), (0,0,0), 1, 1, 1, 1, "refraction")
    R2 = Rayon((0, 0, 0), (0, 0, 0), 2, 1, 1, 1, "refraction")
    R3 = Rayon((0, 0, 1), (0, 0, 0), 2, 1, 1, 1, "refraction")




