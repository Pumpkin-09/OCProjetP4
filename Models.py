import random
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


class Match:

    def __init__(self, liste_match):
        self.joueur_1 = liste_match[0]
        self.joueur_2 = liste_match[1]
        self.resultat = None

    def attribution_point(self, resultat):
        if resultat == "1":
            self.joueur_1.score += 1
            score_1 = 1
            score_2 = 0

        elif resultat == "2":
            self.joueur_2.score += 1
            score_1 = 0
            score_2 = 1

        else:  # match nul
            self.joueur_1.score += 0.5
            self.joueur_2.score += 0.5
            score_1 = 0.5
            score_2 = 0.5

        resultat = ([self.joueur_1.numero_ine, score_1], [self.joueur_2.numero_ine, score_2])
        return tuple(resultat)


class Tour:

    def __init__(self, liste_des_joueurs, non_joueur=0):
        self.liste_des_joueurs = liste_des_joueurs
        self.non_joueur = non_joueur

    def randomiseur_tour1(self):
        random.shuffle(self.liste_des_joueurs)

    def triage_par_points(self):
        self.liste_des_joueurs.sort(key=lambda item: item.score, reverse=True)
        
    def triage_par_points_decroissant(self):
        self.liste_des_joueurs.sort(key=lambda item: item.score)

    def association_joueurs(self, tournoi):
        impair = None
        while True:
            liste_travail = self.liste_des_joueurs.copy()
            if len(liste_travail) % 2 != 0:
                impair = random.randint(0, len(liste_travail)-1)
                self.non_joueur = liste_travail[impair]
                del liste_travail[impair]
            i = 1
            liste_de_matchs = []
            try:
                while len(liste_travail) > 0 and i != len(liste_travail):
                    liste1 = [liste_travail[0].numero_ine, liste_travail[i].numero_ine]
                    liste2 = [liste_travail[i].numero_ine, liste_travail[0].numero_ine]
                    if liste1 in tournoi.liste_des_tours["adversaire"] or liste2 in tournoi.liste_des_tours["adversaire"]:
                        i += 1
                    else:
                        match = [liste_travail[0], liste_travail[i]]
                        liste_de_matchs.append(match)
                        tournoi.liste_des_tours["adversaire"].append(liste1)
                        del liste_travail[i]
                        del liste_travail[0]
                        i = 1
                return liste_de_matchs
            except IndexError:
                return None
