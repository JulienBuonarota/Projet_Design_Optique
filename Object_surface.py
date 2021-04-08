##
import ast

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
        :param origine: (x, y, z)
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


