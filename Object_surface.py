##

# class new-style defini avec C(object) -> dans python 3, c'est new style par defaut
class Sphere():
    def __init__(self, R=10, origine=None, angles=None):
        self.rayon = R
        if origine == None:
            self.origine = (0, 0, 0)
        else:
            self.origine = origine
        if angles == None:
            self.angles = (0, 0, 0)
        else:
            self.angles = angles

S = Sphere(1)
# methode objet.__dic__ pour acceder a l'objet en tant que dict
# TODO inclure plusieur representation mathematique de la sphere (voir livre)
# TODO instancier quelque sphere pour que berengere puisse tracer des trucs

