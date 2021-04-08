import csv
import os
import ast
import pickle

class parametre_etude():
    def __init__(self):
        self.longueur_onde = 0
        self.champs = []
        self.unite = ""

    def __repr__(self):
        return "Paramètres d'études: \n longueur d'onde = {} \n champs = {} \n unite = {}"\
            .format(self.longueur_onde, self.champs, self.unite)

    def write_csv(self, dossier):
        d = self.__dict__
        with open(os.path.join(dossier, "parametre_etude.csv"), 'w') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=d.keys())
            # TODO modifier l'ecriture de la liste comme dans la methode d'ecriture des dioptre
            #  pour eviter la conversion un peu bete a la lecture (et faciliter le travail d'edition de la liste
            csv_writer.writeheader()
            csv_writer.writerow(d)

    def read_csv(self, dossier):
        with open(os.path.join(dossier, "parametre_etude.csv"), 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = csv_reader.__next__()
            self.longueur_onde = ast.literal_eval(data["longueur_onde"])
            # la list ne peut pas etre ecrit avec des virgules dans une cellule de fichier csv
            # la liste de champ doit donc etre ecrite avec des espace à la place
            self.champs = ast.literal_eval(data["champs"].replace(" ", ","))
            self.unite = data["unite"]

    def save(self, dossier):
        with open(os.path.join(dossier, "parametre_etude.pickle"), 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def load(self, dossier):
        with open(os.path.join(dossier, "parametre_etude.pickle"), 'rb') as file:
            data = pickle.load(file)
        return data


if __name__ == "__main__":
    objet = parametre_etude()
    #objet.write_csv("test")
    objet.read_csv("test")
    print(objet)

    objet.save("test")
    objet2 = parametre_etude.load("test")
    print(objet2)
