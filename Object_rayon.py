# TODO Instancier quelques rayons a la main pour que berengere puisse avoir des truc a tracer
# TODO exemple berengere


class Rayon():
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

    def set_arrive(self, arrive, nb_surface_arrive):
        self.arrive = arrive
        self.surface_arrive = nb_surface_arrive
        # passage dans le set des rayons calcule
        self.__class__.instances_non_calcule.difference_update({self})
        self.__class__.instances_calcule.add(self)
    # TODO methode de tracer matplotlib (voir script trace rayon pour des idées)

# TODO trouver comment chercher rayon d'un chemin, d'un champ
#  soit recherche possible dans le set
#  sinon utilisation de dataframe
#  et/ou reference du rayon suivant, precedent dans le rayon
if __name__ == "__main__":
    for i in range(3):
        r = Rayon(1, 2, 3, 4, 5, 6)
    r.set_arrive(1, 2)
    print(r.instances_calcule)
    print(r.instances_non_calcule)

