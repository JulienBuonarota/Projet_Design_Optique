# TODO Script de plot system
"""
Script de plot d'un system optique

input -> le dossier du system a plot

"""
import Object_system as osys
## TODO recuperation de l'argument du script -> le dossier
dossier = ""
## TODO creation du system optique a partir des deux fichiers csv
#  dioptre.csv et parametre_etude.csv
# chargement du systeme
system = osys.system_optique.load(dossier)
# lecture csv

## TODO tracage des rayons
## TODO plot du system complet
