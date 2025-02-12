import json
import os


class Joueur:

    def __init__(self, numero_ine, nom, prenom, date_naissance, score=0.0):

        self.numero_ine = numero_ine
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.score = score

    def __repr__(self):
        return (f"{self.nom} {self.prenom}, date de naissance:{self.date_naissance} numero INE:{self.numero_ine}\n")


class Tournoi:

    def __init__(self, nom, lieu, date_de_debut, date_de_fin, remarque, nombre_de_tours=4,
                 tour_actuel=0, liste_des_joueurs=[], liste_des_tours={"round": {}, "adversaire": []}):

        self.nom = nom
        self.lieu = lieu
        self.date_de_debut = date_de_debut
        self.date_de_fin = date_de_fin
        self.remarque = remarque
        self.nombre_de_tours = nombre_de_tours
        self.tour_actuel = tour_actuel
        self.liste_des_joueurs = liste_des_joueurs
        self.liste_des_tours = liste_des_tours

    def sauvegard(self):
        # Remplacement des anciennes donnees liste des joueurs, tour actuel et liste des tours dans le fichier json
        joueurs = []
        dossier = "tournoi"
        date_nom = self.date_de_debut.replace("/", "")
        fichier_tournoi = f"tournoi_{self.nom}_{self.lieu}_{date_nom}.json"
        chemin_fichier = os.path.join(dossier, fichier_tournoi)
        for joueur in self.liste_des_joueurs:
            joueur_ine = joueur.numero_ine
            joueur_score = joueur.score
            joueurs.append([joueur_ine, joueur_score])
        with open(chemin_fichier, "r") as f:
            settings = json.load(f)

        settings["liste des joueurs"] = joueurs
        settings["tour actuel"] = self.tour_actuel
        settings["liste des tours"] = self.liste_des_tours

        with open(chemin_fichier, "w") as f:
            json.dump(settings, f, indent=4)
