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

##  creation du system optique a partir des deux fichiers csv
system = osys.system_optique(args.dossier, "")
system.read_csv_dioptres()

# recuperation de la surface stop
surface_stop = system.dioptres[-1]
surface_stop.origine = list(surface_stop.origine)
z0 = surface_stop.origine[2]
# calcul taille spot selon axe z
rayon_spot = []
z = np.linspace(-5, 5, 20)
for i in z:
    
    surface_stop.origine[2] = z0 + i
    spots = ssd.main(system)
    print(len(system.rayon.instances))
    rayon_spot.append(oma.rayon_centroid(spots[:, 0], spots[:,1]))
    # reset des rayons
    system.rayon.instances = []
    system.rayon.nb_calcul = 0


plt.plot(z + z0, rayon_spot)
plt.show()
