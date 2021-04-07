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

## Creation des elements de base du system

## Lecture d'un systeme optique et interpretation
# TODO avoir la possibilite d'avoir input_string comme parametre d'entrée d'éxecution du script

input_string = " () _ () _ () |"
dossier = "test"

system = Object_system.system_optique(dossier, input_string)


## compter les elements
# regex_dioptres = re.compile("[()]")
# nb_dioptres = len(regex_dioptres.findall(input_string))
#
# ## creer la liste des elements (avec les object aproprie)
# # TODO a placer dans la classe system, quand elle est faite
#
#
# ## creation du fichier de configuration/specification
# # TODO remplacer par la methode de la classe system, quand elle est faite
# d = [i.__dict__ for i in Surfaces]
# # Creation du fichier csv
# with open("Surfaces.csv", 'a') as csv_file:
#     csv_writer = csv.DictWriter(csv_file, fieldnames=d[0].keys())
#     csv_writer.writeheader()
#     for s in d:
#         csv_writer.writerow(s)
#
# ## Lecture du csv et ecriture pickel
# # TODO modifier par la methode de la classe system quand elle est faite
# data = pd.read_csv("systeme_08_04_2021/Surfaces.csv")
#
# for i in ["origine", "angles"]:  # parametre d'origine et d'axe du repere associer a chaque surface
#     data[i] = [ast.literal_eval(i) for i in data[i]]
# with open("data_pickel", "wb") as file:
#     pickle.dump(data, file)


