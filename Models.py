from datetime import date
import random
import json


class Joueur:

    def __init__(self, nom_de_famille, prenom, date_de_naissance, numero_ine, liste_d_adversaire, nombre_de_points=0.0):
            
        self.nom_de_famille = nom_de_famille
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.numero_ine = numero_ine
        self.liste_d_adversaire = liste_d_adversaire = []
        self.nombre_de_points = nombre_de_points


class Tournoi:

    def __init__(self, nom, lieu, date_de_debut, date_de_fin, tour_actuel, liste_des_tours, liste_des_joueurs, remarque, nombre_de_tours=4):
     
        self.nom = nom
        self.lieu = lieu
        self.date_de_debut = date_de_debut
        self.date_de_fin = date_de_fin
        self.tour_actuel = tour_actuel
        self.liste_des_tours = liste_des_tours
        self.liste_des_joueurs = liste_des_joueurs
        self.remarque = remarque
        self.nombre_de_tours = nombre_de_tours


class Match:

    def __init__(self, joueur_1, joueur_2, score_1=0.0, score_2=0.0):

        self.joueur_1 = joueur_1
        self.joueur_2 = joueur_2
        self.score_1 = score_1
        self.score_2 = score_2


    def ajouter_score(self, Joueur, score):
        if self.joueur_1.gagnant:
            self.score_1 = 1
            self.score_2 = 0
        if self.joueur_2.gagnant:
            self.score_1 = 0
            self.score_2 = 1
        else:
            self.score_1 = 0.5
            self.score_2 = 0.5
            
        resultat = ([self.joueur_1, self.score_1], [self.joueur_2, self.score_2])
        return tuple(resultat)


class Tour:
    tour_en_cours = 0
    def __init__ (self, numero_du_tour):
        Tour.tour_en_cours += 1
        self.numero_du_tour = numero_du_tour
    
    def randomiseur_tour1(self, list_de_joueurs):
        liste_de_joueurs_alleatoire = random.shuffle(list_de_joueurs)
        return liste_de_joueurs_alleatoire
        
    def creation_des_matchs(self, liste_de_joueurs):
        liste_de_joueurs_triees = sorted(liste_de_joueurs, key=lambda joueur: joueur.score, reverse=True)
        liste_des_matchs = []
        i = 1

        if len(liste_de_joueurs_triees)%2 != 0:
            impair = random.randint(0, len(liste_de_joueurs_triees-1))
            del liste_de_joueurs_triees[impair]

        while len(liste_de_joueurs_triees) > 0 and i != len(liste_de_joueurs_triees):
            if liste_de_joueurs_triees[0].liste_d_adversaire in liste_de_joueurs_triees[i].numero_ine:
                i += 1
            else :
                match = Match(liste_de_joueurs_triees[0], liste_de_joueurs_triees[i])
                liste_des_matchs.append(match)
                liste_de_joueurs_triees[0].liste_d_adversaire.append(liste_de_joueurs_triees[i].numero_ine)
                liste_de_joueurs_triees[i].liste_d_adversaire.append(liste_de_joueurs_triees[0].numero_ine)
                del liste_de_joueurs_triees[0:i]
                i = 1
        
        return liste_des_matchs

    

fichier_joueurs = "joueurs.json"

with open(fichier_joueurs, "r") as f:
    donnees_joueurs = json.load(f)

    liste_joueurs = []
    for j in donnees_joueurs:
        nom = j.get("nom")
        prenom = j.get("prenom")
        date_de_naissance = j.get("date de naissance")
        numero_ine = j.get("numero ine")

        joueur = Joueur(nom, prenom, date_de_naissance, numero_ine)
        liste_joueurs.append(joueur)




        







