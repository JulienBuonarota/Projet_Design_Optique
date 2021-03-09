##

class Sphere():
    def __init__(self, R, origine=None, angles=None):
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
