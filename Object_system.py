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
        d = [i.__dict__ for i in self.dioptres]
        # Creation du fichier csv
        with open(os.path.join(self.dossier, "dioptres.csv"), 'w') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=d[0].keys())
            csv_writer.writeheader()
            for s in d:
                csv_writer.writerow(s)

    def read_csv_dioptres(self):
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
        # TODO tracer tout les rayons non calculés jusqu'à la surface N
        #  creer au fur et à mesure les rayons refracte
        #  utiliser la methode de refraction
        pass

    # TODO fct qui plot le système entier
    #  utilisant les fct representation des differents obj
    #  a prenant les styles depuis un fichier de config
