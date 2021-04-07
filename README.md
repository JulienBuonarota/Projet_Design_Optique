# Projet_Design_Optique
Projet de logiciel de calcul optique en python.

C’est ici qu’on écrit la structure du projet.
## Rendu intermédiaire du 08/04/2021
Input utilisateur : 
- Système optique = " () _ () _ ())"
- Que des surfaces sphériques, de rayon variables
- A réaliser : 
  - Interpréation de la string d'entre (Julien)
  - Plot des dioptres façon code V (Bérengère)
  - Tracer les rayons (Julien)
  - Plot des rayons (Bérengère)
    
https://matplotlib.org/stable/gallery/mplot3d/lines3d.html

## Liens importants
Drop box : https://www.dropbox.com/sh/dlpbtrsl7c5js0k/AACg2vRWNldNmR4MMAzrymQGa?dl=0 

Github : https://github.com/JulienBuonarota/Projet_Design_Optique

Procédure de Push Pull sur le repo github : 

Découverte python : https://www.codewars.com/
## Idées
### Integration Git
Avoir une intégration git pour rapidement tester des design en créant des branch et commit rapidement.
Utiliser la bibliothèque Magit d'emacs pour gérer ça.

Avoir une complétion automatique des messages de commit avec les infos de performances du système. Avoir des
fonctions de recherche dans l'historique des commits celon certain critères, exp : meilleur FTM, moindre coût, meilleur
correction d'une abération spécifique, ...
## Définition du système du système optique (Julien)
La définition du système passe par l’écriture d’une chaîne de caractère utilisant les symbols du clavier pour représenter les dioptres:

Exemples :
- Lentille simple  “ () “
- Plus de lentilles “ (() () )) “
- autre dispo

Les symbols disponibles : & ~ " # ' { ( [ ] ) - | _ \ / @ = + , ; . : § *

) créer un dioptre concave, ( un dioptre convexe. C’est juste la valeur par défaut à la 
création qui est affecté, par le suite n’importe quelle valeur peut être sélectionner

| définie une ouverture (circulaire par défaut mais qui peut être de forme quelconque) 
qui permet de définir des pupilles


[ et ] représentent des miroirs

L’ordre des objets dans la chaîne de caractère représente l’ordre des surfaces en terme 
de propagation de la lumière (dans la logique du sequencial ray tracing)
Spécification des dioptres, ou groupe de dioptres

{"Dioptre 1":{

   "Rayon de courbure": 100 mm

Elements définissant une surface: 
Type: Sphere, paraboles, …

Cas Sphère:
 - Rayon:
 - Coordonnées du repère par rapport à un autre repère. Par défaut c'est le repère 
de la lentille précédente, mais ça peut être spécifié autrement.
   
Idées des fonctionnalités: 
- coloration des groupes de lentilles
- division d‘une lentille en deux lentilles
- Une surface peut suivre une surface du même type


### Class Surface : Object_surface.py
Class définissant des surfaces.
Chaque surface doit en hériter

méthodes à définir : 
- écriture .txt pour édition humaine
- écriture .csv pour plot
- init depuis un dictionnaire

### Class Système
Class pour gérer le système optique compelt.
Y charger les spécifications du systèmes telque champs, longueurs d'ondes, etc ...


## Capacité à plot les différents éléments du système (Bérengère)
Plot le système optique. Plot les dioptres.

Utiliser la librairie **matplotlib**.

https://www.youtube.com/watch?v=UO98lJQ3QGI&list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_

Il faut regarder la video sur le live plotting (video 9)

Ecriture des donnes dans un fichier csv et lecture par le script de plot.


## Calculer la trajectoire des rayons (Julien)

## Analyse du système

## Optimisation du système

## Fonctionnement général du logiciel
### première version avec lancé de rayons
1) [utilisateur] création d'un fichier texte avec la string décrivant le système
2) Création a partir de ce fichier texte de
   - fichier csv de description des surfaces
   - fichier csv de description des parametre d'etudes
3) Editions de ces fichiers csv par l'utilisateur
4) A partir des deux fichier csv (system, parametre d'etude)
   - creation des rayons initiaux
   - calcul de la propagation des rayons
   - Plot du système optique
     - avec ou sans rayons
     - selon la coupe X ou Y 
