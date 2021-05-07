""" Dans le main

Lecture de la chaine de définition, exp : " ((  () | ()"

Creation des csv d'edition des surface et csv parametre systeme

"""
## import
import re
import csv
import pandas as pd
import ast
import pickle
import Object_system
import pathlib
import argparse
import os

## Lecture d'un systeme optique et interpretation
parser = argparse.ArgumentParser(prefix_chars='-')
parser.add_argument("-d", "--dossier",
                    help="Dossier contenant l'ensemble des fichiers du system",
                    required=True)
parser.add_argument("-s", "--system_string",
                    help="String decrivant les dioptres du system",
                    required=True)
args = parser.parse_args()

# creation du dossier
try:
    os.mkdir(args.dossier)
except FileExistsError:
    print("Dossier : {} deja  existant".format(args.dossier))


system = Object_system.system_optique(args.dossier, args.system_string)
system.create_dioptres()
system.write_csv_dioptres(system.dossier)
system.save(system.dossier)

## Chargement apres modification par l'utilisateur et enregistrement au format pickle
# system = Object_system.system_optique.load(dossier)
# system.read_csv_dioptres()
# system.save(system.dossier)


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


