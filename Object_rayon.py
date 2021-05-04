##
import numpy as np
import matplotlib.pyplot as plt

##
class Rayon():
    # TODO remplacer par dataframe
    instances_calcule = set()
    instances_non_calcule = set()


    def __init__(self, origine, direction, chemin, champ, longueur_onde, nb_surface_refraction):
        self.origine = origine
        self.direction = direction
        self.chemin = chemin  # meme que le rayon incident
        self.champ = champ  # meme que le rayon incident
        self.longueur_onde = longueur_onde # meme que le rayon incident
        self.surface_origine = nb_surface_refraction
        # ajout a la liste des instances de la classe
        self.__class__.instances_non_calcule.add(self)

    def __repr__(self):
        try:
            return "rayon d'origine = {}, de direction {} et d'arrive = {}"\
                .format(self.origine, self.direction, self.arrive)
        except AttributeError:
            return "rayon d'origine = {}, de direction {}" \
                .format(self.origine, self.direction)


    def set_arrive(self, arrive, nb_surface_arrive):
        self.arrive = arrive
        self.surface_arrive = nb_surface_arrive
        # passage dans le set des rayons calcule
        self.__class__.instances_non_calcule.difference_update({self})
        self.__class__.instances_calcule.add(self)

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
            P = P - 4*C
            # Creation du rayon de meme num de champ mais de chemin different
            r = Rayon(P, C, count, num_champ, longueur_onde, nb_surface_refraction)
        return r
##
# TODO trouver comment chercher rayon d'un chemin, d'un champ
#  soit recherche possible dans le set
#  sinon utilisation de dataframe
#  et/ou reference du rayon suivant, precedent dans le rayon

# TODO methode de creation de rayon en mode "champ" - a tester

# TODO classmethod permettant d'obtenir une liste des representation de tout les rayons
#  voir ca comme une dataframe ? ou avoir ca en option ? pour auqnd il est necessaire de faire des plot particulier.
if __name__ == "__main__":
    # R = Rayon((0,0,0), (0,0,0), 1, 1, 1, 1)
    R = Rayon.creation_champ(10, 3, 20*3.1415/180, 1, 1, 0, np.array((0,0,3)))
    print(R.instances_non_calcule)
    ##
    for i in R.instances_non_calcule:
        plt.plot(i.represente())
    ##

