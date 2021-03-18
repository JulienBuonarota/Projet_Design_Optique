""" Dans le main

Lecture de la chaine de définition, exp : " ((  () | ()"
Déduction des groupes
Création du fichier txt d'édition des surfaces

lecture du fichier txt et creation d'un csv pour le plot

"""
## import
import re
import Object_surface
import csv
import pandas as pd
import ast
import pickle
## Lecture d'un systeme optique et interpretation

input_string = " () _ () _ () |"

## compter les elements
regex_dioptres = re.compile("[()]")
nb_dioptres = len(regex_dioptres.findall(input_string))

## creer la liste des elements (avec les object aproprie)
Surfaces = [Object_surface.Sphere() for i in range(nb_dioptres)]

## creation du fichier de configuration/specification
d = [i.__dict__ for i in Surfaces]
# Creation du fichier csv
with open("Surfaces.csv", 'a') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=d[0].keys())
    csv_writer.writeheader()
    for s in d:
        csv_writer.writerow(s)

## Lecture du csv et ecriture  pickel
data = pd.read_csv("systeme_08_04_2021/Surfaces.csv")

for i in ["origine", "angles"]:
    data[i] = [ast.literal_eval(i) for i in data[i]]
with open("data_pickel", "wb") as file:
    pickle.dump(data, file)


