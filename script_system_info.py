import Object_system
import argparse


parser = argparse.ArgumentParser(prefix_chars='-')
parser.add_argument("-d", "--dossier",
                    help="Dossier contenant l'ensemble des fichiers du system",
                    required=True)

args = parser.parse_args()

## Chargement apres modification par l'utilisateur et enregistrement au format pickle
system = Object_system.system_optique.load(args.dossier)
system.read_csv_dioptres()
system.save(system.dossier)


