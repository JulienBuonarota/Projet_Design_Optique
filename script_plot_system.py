# TODO Script de plot system
"""
Script de plot d'un system optique

input -> le dossier du system a plot

"""
import Object_system as osys
import argparse


## recuperation de l'argument du script -> le dossier
parser = argparse.ArgumentParser(prefix_chars='-')
parser.add_argument("-d", "--dossier",
                    help="Dossier contenant l'ensemble des fichiers du system",
                    required=True)
args = parser.parse_args()

## TODO creation du system optique a partir des deux fichiers csv
system = osys.system_optique(args.dossier, "")
system.read_csv_dioptres()
system.creation_rayons([400, 800], [0])

## TODO tracage des rayons
system.propagation()
## TODO plot du system complet
system.plot()
