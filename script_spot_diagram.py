"""
Script de plot d'un system optique

input -> le dossier du system a plot

"""
##
import Object_system as osys
import argparse
import numpy as np
import matplotlib.pyplot as plt
import Object_rayon as oray
import Outils_math as oma
import copy

# TODO avoir le champ et longueur d'onde comme parametre d'entre du main et script

def main(system, longueur_onde, champ):
    # creation des rayons selon x et y
    origine = copy.deepcopy(system.dioptres[0].origine)
    origine = list(origine)
    # longueur_onde, champ = system.conf.longueur_onde, system.conf.champs
    for l in longueur_onde:
        for count, c in enumerate(champ):
            for i in np.linspace(-5, 5, 10):
                origine[0] = i
                R = oray.Rayon.creation_champ(nb_rayon=5, hauteur=5, angle=c*3.1415/180,
                                              num_champ=c, longueur_onde=l,
                                              nb_surface_refraction=0,
                                              origine_surface=origine)
    system.rayon = R
    
    ## tracage des rayons
    system.propagation()
    
    ## plot du spot diagram
    instances = system.rayon.instances
    nb_surfaces = [i.surface_origine for i in instances]
    nb_surface_max = max(set(nb_surfaces))
    # recuperation des intersection avec la surface stop
    spots = np.array([i.arrive for i in instances if (i.surface_origine == nb_surface_max)])
    
    return spots

if __name__ == "__main__":
    ## recuperation de l'argument du script -> le dossier
    parser = argparse.ArgumentParser(prefix_chars='-')
    parser.add_argument("-d", "--dossier",
                        help="Dossier contenant l'ensemble des fichiers du system",
                        required=True)
    parser.add_argument("-c", "--champ",
                    help="Champ d'etudes, en degrees")
    parser.add_argument("-l", "--longueur_onde",
                        help="Longueur d'onde d'etudes, en nm")

    args = parser.parse_args()
    

        
    ##  creation du system optique a partir des deux fichiers csv
    system = osys.system_optique(args.dossier, "")
    system.read_csv_dioptres()

    # test argument optionel
    if args.longueur_onde is None:
        longueur_onde = [system.conf.longueur_onde[0]]
    else:
        longueur_onde = args.longueur_onde

    if args.champ is None:
        champ = [system.conf.champs[0]]
    else:
        champ = args.champ
        
    # calcul spot
    spots = main(system, longueur_onde, champ)
    rayon_spot = oma.rayon_centroid(spots[:, 0], spots[:,1])
    
    plt.plot(spots[:, 0], spots[:, 1], 'o')
    plt.xlabel("x (en {})".format(system.conf.unite))
    plt.ylabel("y (en {})".format(system.conf.unite))
    plt.title("Spot diagram, r = {:1f} {}".format(rayon_spot, system.conf.unite))
    plt.grid()
    plt.show()
