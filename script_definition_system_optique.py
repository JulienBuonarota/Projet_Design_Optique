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
# system.save(system.dossier)


