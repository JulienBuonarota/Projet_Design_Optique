""" Dans le main

Lecture de la chaine de définition, exp : " ((  () | ()"
Déduction des groupes -> pas utile ici ? a faire dans emacs comme interface
Création du fichier txt d'édition des surfaces

lecture du fichier txt et creation d'un csv pour le plot

"""
## import
import re
import csv
import pandas as pd
import ast
import pickle
import Object_system
import pathlib

## Lecture d'un systeme optique et interpretation
# TODO avoir la possibilite d'avoir input_string comme parametre d'entrée d'éxecution du script

input_string = " () _ () _ () |"
dossier = "systeme_08_04_2021"

system = Object_system.system_optique(dossier, input_string)

## Chargement apres modification par l'utilisateur et enregistrement au format pickle
system = Object_system.system_optique.load(dossier)
system.read_csv_dioptres()
system.save(system.dossier)


## compter les elements
# regex_dioptres = re.compile("[()]")
# nb_dioptres = len(regex_dioptres.findall(input_string))
#
# ## creer la liste des elements (avec les object aproprie)
#
#
# ## creation du fichier de configuration/specification
# d = [i.__dict__ for i in Surfaces]
# # Creation du fichier csv
# with open("dioptres.csv", 'a') as csv_file:
#     csv_writer = csv.DictWriter(csv_file, fieldnames=d[0].keys())
#     csv_writer.writeheader()
#     for s in d:
#         csv_writer.writerow(s)
#
# ## Lecture du csv et ecriture pickel
# data = pd.read_csv("systeme_08_04_2021/dioptres.csv")
#
# for i in ["origine", "angles"]:  # parametre d'origine et d'axe du repere associer a chaque surface
#     data[i] = [ast.literal_eval(i) for i in data[i]]
# with open("data_pickel", "wb") as file:
#     pickle.dump(data, file)


