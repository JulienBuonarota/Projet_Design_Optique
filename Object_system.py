"""
Object regroupant les element du system

"""
import os
import pickle
import re
import csv
import ast
import pandas as pd
import Object_surface
import Object_parametre_etude
import Object_rayon as oray
import Outils_lanceur_rayon as olray
import matplotlib.pyplot as plt

# TODO methode load a partir d'un csv, pour pouvoir prendre en compte l'ajout
#  de surface, ou deletion, par l'utilisateur (qui edite le csv)

class system_optique():
    regex_dioptres = re.compile("[()/|\\\]")
    # regex_dioptres = re.compile("[()]")

    def __init__(self, dossier, system_string):
        self.dossier = dossier
        self.system_string = system_string
        # Parametres du system
        # TODO a remplacer par le fichier .py
        #   self.parametres = Object_parametre_etude.parametre_etude()
        #   self.parametres.write_csv(self.dossier)
        # Dioptres du system
        self.create_dioptres()
        # TODO methode de creation des rayon initiaux (d'après les paramètres d'étude)
        self.write_csv_dioptres(self.dossier)

        # self.save(self.dossier)

    def create_dioptres(self):
        # TODO reconnaitre sphere et plan
        # TODO ajout surface stop a la fin de la liste des dioptres
        # fonction probablement plus complexe une fois les dioptres plus divers
        nb_dioptres = len(self.regex_dioptres.findall(self.system_string))
        self.dioptres = [Object_surface.Sphere() for i in range(nb_dioptres)]
        self.dioptres = []
        for i in self.regex_dioptres.findall(self.system_string):
            if (i == "(" or i == ")"):
                self.dioptres.append(Object_surface.Sphere())
            # elif(i == "\\" or i == "/"):
            #     self.dioptres.append(Object_surface.Miroir())
            elif (i == "¦" or i == "\\" or i == "/"):
                self.dioptres.append(Object_surface.Plan())
            else:
                print("Type de surface non reconnu")

    def write_csv_dioptres(self, dossier):
        #  # TODO remplacer par une dataframe, permet de facilement concatener toute les surfaces
        #  #  (meme si pas meme attributs)
        #  #  ATTENTION, SEPARATEUR = |
        #  print(self.dioptres)
        #  d = [i.get_dict() for i in self.dioptres]
        #  # Creation du fichier csv
        #  with open(os.path.join(self.dossier, "dioptres.csv"), 'w') as csv_file:
        #      csv_writer = csv.DictWriter(csv_file, fieldnames=d[0].keys())
        #      csv_writer.writeheader()
        #      for s in d:
        #          csv_writer.writerow(s)
        df = pd.DataFrame()
        for d in self.dioptres:
            df = df.append(d.get_dict(), ignore_index=True)
        nom_fichier = os.path.join(self.dossier, "dioptres.csv")
        df.to_csv(nom_fichier, sep="|")

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
        while oray.Rayon.nb_calcule > 0:
            for rayon in self.rayon.instances:  # oray.Rayon.instances:
                if rayon.calcule is False:
                    olray.interaction(rayon, self.dioptres[rayon.surface_origine])

    def plot(self):
        for i in self.dioptres:
            plt.plot(*i.represente(), color='k')
        for r in self.rayon.instances:
            plt.plot(*r.represente(), color='r')
        plt.grid()
        plt.show()


if __name__ == "__main__":
    # TODO fct general qui concatene des regex et les cherches ds un string
    import re
    system_string = " () |/ || (|\\ "
    regex_dioptres = re.compile("[()/|\\\]")
    nb_dioptres = len(regex_dioptres.findall(system_string))
    print(system_string)
    print(nb_dioptres)
    for i in regex_dioptres.findall(system_string):
        print(i)
