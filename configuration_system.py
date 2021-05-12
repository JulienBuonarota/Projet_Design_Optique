"""
     Parametres d'etudes du system optique
"""
unite = "mm"
# list des longueurs d'ondes d'etudes
longueur_onde = [200, 800]  # type: [float]
longueur_onde_unite = "nm"  # type: string

# Angles des rayons en entree du system, en deg
champs = [0, -20]  # type: [float]
#   nb de rayons par unite
champs_densite = 5  # type: int


"""
    Spot Diagram
"""
# echantillonnage de l'espace de depart, carre ou circulaire
SD_type_echantillonage = "carre"
