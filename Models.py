from datetime import date
import random
import json
from enum import Enum


class Joueur:

    def __init__(self, nom_de_famille, prenom, date_de_naissance, numero_ine, nombre_de_points=0.0, liste_d_adversaire=[]):
        self.nom_de_famille = nom_de_famille
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.numero_ine = numero_ine
        self.nombre_de_points = nombre_de_points
        self.liste_d_adversaire = liste_d_adversaire


class Tournoi:

    def __init__(self, nom, lieu, date_de_debut, date_de_fin, remarque, nombre_de_tours=4, liste_des_joueurs=[], tour_actuel=0, liste_des_tours=[]):
        self.nom = nom
        self.lieu = lieu
        self.date_de_debut = date_de_debut
        self.date_de_fin = date_de_fin
        self.remarque = remarque
        self.nombre_de_tours = nombre_de_tours
        self.liste_des_joueurs = liste_des_joueurs
        self.tour_actuel = tour_actuel
        self.liste_des_tours = liste_des_tours 


class Match:

    def __init__(self, liste_joueur):
        self.joueur_1 = liste_joueur[0]
        self.joueur_2 = liste_joueur[1]
        self.resultat = None

    def attribution_point(self, resultat):
        if resultat == "1":
            self.joueur_1.nombre_de_points += 1
            score_1 = 1
            score_2 = 0
        
        elif resultat == "2":
            self.joueur_2.nombre_de_points += 1
            score_1 = 0
            score_2 = 1
        
        else: # match nul
            self.joueur_1.nombre_de_points += 0.5
            self.joueur_2.nombre_de_points += 0.5
            score_1 = 0.5
            score_2 = 0.5

        resultat = ([self.joueur_1, score_1], [self.joueur_2, score_2])
        return tuple(resultat)


class Tour:

    def __init__ (self, liste_de_joueurs, numero_round):
        self.numero_round = numero_round
        self.liste_de_joueurs = liste_de_joueurs
    
    def randomiseur_tour1(self):
        for clear_liste_adversaire in self.liste_de_joueurs:
            clear_liste_adversaire.liste_d_adversaire.clear()
        random.shuffle(self.liste_de_joueurs)
        
    def triage_par_points(self):
        self.liste_de_joueurs.sort(key=lambda joueur: joueur.nombre_de_points, reverse=True)

    def association_joueurs(self):
        liste_travail = self.liste_de_joueurs.copy()
        if len(liste_travail)%2 != 0:
            impair = random.randint(0, len(liste_travail)-1)
            del liste_travail[impair]
        i = 1
        liste_des_matchs = []
        while len(liste_travail) > 0 and i != len(liste_travail):
            if liste_travail[0].numero_ine in liste_travail[i].liste_d_adversaire:
                i += 1
            else :
                liste_travail[0].liste_d_adversaire.append(liste_travail[i].numero_ine)
                liste_travail[i].liste_d_adversaire.append(liste_travail[0].numero_ine)
                match = (liste_travail[0], liste_travail[i])
                liste_des_matchs.append(match)
                del liste_travail[i]
                del liste_travail[0]
                i = 1
        return liste_des_matchs

    def enregistrement_resultat(self):
        fichier = "joueurs.json"
        with open(fichier, "r") as f:
            settings = json.load(f)
        for enregistrement in self.liste_de_joueurs:
            settings[enregistrement.numero_ine]["nombre_de_points"] += enregistrement.nombre_de_points            
            with open(fichier, "w") as f:
                json.dump(settings, f, indent=4)