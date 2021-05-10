import matplotlib.pyplot as plt
import script_spot_diagram as ssd
import Outils_math as oma
import Object_system as osys
import numpy as np
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

# recuperation de la surface stop
surface_stop = system.dioptres[-1]
surface_stop.origine = list(surface_stop.origine)
z0 = surface_stop.origine[2]
# calcul taille spot selon axe z
rayon_spot = []
for i in np.linspace(-5, 5, 20):
    surface_stop.origine[2] = surface_stop.origine[2] + i
    spots = ssd.main(system)
    rayon_spot.append(oma.rayon_centroid(spots[:, 0], spots[:,1]))

plt.plot(np.linspace(-5, 5, 20) + zo, rayon_spot)
plt.show()
