

class Materiaux():
    def __init__(self, n0, l0, a):
        self.n0 = n0
        self.l0 = l0
        self.a = a

    def indice(self, l):
        # l: longueur d'onde en nm
        return self.n0 + self.a*(l - self.l0)

AIR = Materiaux(1, 1, 0)
VERRE = Materiaux(1.5, 500, 1e-3)
# TODO prendre des valeurs realistes pour l'indice de l'air et l'eau
