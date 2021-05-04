"""
Object regroupant les element du system

"""
import os
import pickle
import re
import csv
import ast
import Object_surface
import Object_parametre_etude
import Object_rayon as oray
import Outils_lanceur_rayon as olray

class system_optique():
    regex_dioptres = re.compile("[()]")

    def __init__(self, dossier, system_string):
        self.dossier = dossier
        self.system_string = system_string
        # Parametres du system
        self.parametres = Object_parametre_etude.parametre_etude()
        self.parametres.write_csv(self.dossier)
        self.parametres.save(self.dossier)
        # Dioptres du system
        self.create_dioptres()
        # TODO methode de creation des rayon initiaux (d'après les paramètres d'étude)
        self.write_csv_dioptres(self.dossier)

        self.save(self.dossier)

    def create_dioptres(self):
        # TODO reconnaitre sphere et plan
        # fonction probablement plus complexe une fois les dioptres plus divers
        nb_dioptres = len(self.regex_dioptres.findall(self.system_string))
        self.dioptres = [Object_surface.Sphere() for i in range(nb_dioptres)]

    def write_csv_dioptres(self, dossier):
        # TODO remplacer par une dataframe, permet de facilement concatener toute les surfaces
        #  (meme si pas meme attributs)
        #  ATTENTION, SEPARATEUR = |
        d = [i.__dict__ for i in self.dioptres]
        # Creation du fichier csv
        with open(os.path.join(self.dossier, "dioptres.csv"), 'w') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=d[0].keys())
            csv_writer.writeheader()
            for s in d:
                csv_writer.writerow(s)

    def read_csv_dioptres(self):
        # TODO avoir la possibilite d'ecrire l'origine d'une surface d'apres celui de la surface precedente,
        #  par exemple si il y a "+" devant le tuple
        with open(os.path.join(self.dossier, "dioptres.csv"), 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for ligne, d in zip(csv_reader, self.dioptres):
                d.update_from_csv(ligne)

    def save(self, dossier):
        with open(os.path.join(dossier, "system.pickle"), 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def load(self, dossier):
        with open(os.path.join(dossier, "system.pickle"), 'rb') as file:
            data = pickle.load(file)
        return data

    def propagation(self):
        # TODO faire un test de cette methode
        while oray.Rayon.nb_calcule > 0:
            for rayon in oray.Rayon.instances:
                if rayon.calcule is False:
                    olray.interaction(rayon, self.dioptres[rayon.surface_origine])

    # TODO fct qui plot le système entier
    #  utilisant les fct representation des differents obj
    #  a prenant les styles depuis un fichier de config
