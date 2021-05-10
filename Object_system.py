"""
Object regroupant les element du system

"""
import os
import pickle
import re
import csv
import ast
import pandas as pd
import numpy as np
import Object_surface
import Object_parametre_etude
import Object_rayon as oray
import Outils_lanceur_rayon as olray
import Outils_plot as op
import matplotlib.pyplot as plt
import configuration_system


class system_optique():
    regex_dioptres = re.compile("[()/|\\\]")
    # regex_dioptres = re.compile("[()]")

    def __init__(self, dossier, system_string):
        self.dossier = dossier
        self.system_string = system_string
        self.conf = configuration_system



    def creation_rayons(self, longueur_onde, champ):
        for l in longueur_onde:
            for count, c in enumerate(champ):
                R = oray.Rayon.creation_champ(nb_rayon=5, hauteur=5, angle=c*3.1415/180,
                                              num_champ=c, longueur_onde=l,
                                              nb_surface_refraction=0,
                                              origine_surface=self.dioptres[0].origine)
        self.rayon = R

    def create_dioptres(self):
        nb_dioptres = len(self.regex_dioptres.findall(self.system_string))
        self.dioptres = [Object_surface.Sphere() for i in range(nb_dioptres)]
        self.dioptres = []
        for i in self.regex_dioptres.findall(self.system_string):
            if (i == "(" or i == ")"):
                self.dioptres.append(Object_surface.Sphere())
            elif (i == "|" or i == "\\" or i == "/"):
                self.dioptres.append(Object_surface.Plan())
            else:
                print("Type de surface non reconnu")
        self.dioptres.append(Object_surface.Sphere(R=1000, interaction="stop"))

    def write_csv_dioptres(self, dossier):
        df = pd.DataFrame()
        for d in self.dioptres:
            df = df.append(d.get_dict(), ignore_index=True)
        nom_fichier = os.path.join(self.dossier, "dioptres.csv")
        df.to_csv(nom_fichier, sep="|", index=False)

    def read_csv_dioptres(self):
        # TODO avoir la possibilite d'ecrire l'origine d'une surface d'apres celui de la surface precedente,
        #  par exemple si il y a "+" devant le tuple
        nom_fichier = os.path.join(self.dossier, "dioptres.csv")
        df = pd.read_csv(nom_fichier, sep="|")
        df = df.rename(columns=lambda x: x.strip())
        self.dioptres = []
        for i in range(len(df)):
            d = df.loc[i].to_dict()
            if d["type_surface"].strip() == "SPHERE":
                s = Object_surface.Sphere()
                s.update_from_dict(d)
                self.dioptres.append(s)
            elif d["type_surface"].strip() == "PLAN":
                p = Object_surface.Plan()
                p.update_from_dict(d)
                self.dioptres.append(p)
            else:
                print("lecture csv, surface non reconnue")

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
        colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
        style = ['solid', 'dotted', 'dashed', 'dashdot']
        for i in self.dioptres:
            plt.plot(*i.represente(), color='k')
        df_rayon = self.rayon.get_instances_df()
        for count_c, c in enumerate(self.conf.champs):
            for count_l, l in enumerate(self.conf.longueur_onde):
                for i, r in df_rayon[(df_rayon.champ == c) & (df_rayon.longueur_onde == l) & (df_rayon.calcule == True)].iterrows():
                    plt.plot(*op.represente_rayon(r["origine"], r["arrive"]), color=colors[count_l], linestyle=style[count_c])
        plt.grid()
        plt.ylim(-20, 20)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()


if __name__ == "__main__":
    import re
    system_string = " () |/ || (|\\ "
    regex_dioptres = re.compile("[()/|\\\]")
    nb_dioptres = len(regex_dioptres.findall(system_string))
    print(system_string)
    print(nb_dioptres)
    for i in regex_dioptres.findall(system_string):
        print(i)
