"""
Script de plot d'un system optique

input -> le dossier du system a plot

"""
##
import Object_system as osys
import argparse


## recuperation de l'argument du script -> le dossier
parser = argparse.ArgumentParser(prefix_chars='-')
parser.add_argument("-d", "--dossier",
                    help="Dossier contenant l'ensemble des fichiers du system",
                    required=True)
args = parser.parse_args()

##  creation du system optique a partir des deux fichiers csv
system = osys.system_optique(args.dossier, "")
system.read_csv_dioptres()
system.creation_rayons(system.conf.longueur_onde, system.conf.champs)
## tracage des rayons
system.propagation()
## plot du system complet
system.plot()
