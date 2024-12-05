from datetime import date
import random
import json


class Joueur:

    def __init__(self, nom_de_famille, prenom, date_de_naissance, numero_ine, gagnant_match=False, nombre_de_points=0.0, liste_d_adversaire=[]):
            
        self.nom_de_famille = nom_de_famille
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.numero_ine = numero_ine
        self.gagnant_match = gagnant_match
        self.nombre_de_points = nombre_de_points
        self.liste_d_adversaire = liste_d_adversaire


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

    def __init__(self, liste_joueur, score_1=0.0, score_2=0.0):

        self.joueur_1 = liste_joueur[0]
        self.joueur_2 = liste_joueur[1]
        self.score_1 = score_1
        self.score_2 = score_2

    def ajouter_score(self):

        if self.joueur_1.gagnant_match:
            self.score_1 = 1
            self.score_2 = 0
        if self.joueur_2.gagnant_match:
            self.score_1 = 0
            self.score_2 = 1
        else:
            self.score_1 = 0.5
            self.score_2 = 0.5
            
        fichier = "joueurs.json"
        with open(fichier, "r") as f:
            settings = json.load(f)
        settings[self.joueur_1.numero_ine]["nombre_de_points"] += self.score_1
        settings[self.joueur_2.numero_ine]["nombre_de_points"] += self.score_2
        with open(fichier, "w") as f:
            json.dump(settings, f, indent=16)

        resultat = ([self.joueur_1, self.score_1], [self.joueur_2, self.score_2])
        return tuple(resultat)


class Tour:
    tour_actuel = 0
    def __init__ (self, liste_de_joueurs):
        Tour.tour_actuel += 1
        self.liste_de_joueurs = liste_de_joueurs
    
    def randomiseur_tour1(self):
        random.shuffle(self.liste_de_joueurs)
        
    def triage_par_points(self):
        sorted(self.liste_de_joueurs, key=lambda joueur: joueur.nombre_de_points, reverse=True)

    def association_joueurs(self):
        if len(self.liste_de_joueurs)%2 != 0:
            impair = random.randint(0, len(self.liste_de_joueurs)-1)
            del self.liste_de_joueurs[impair]
        i = 1
        liste_des_matchs = []
        while len(self.liste_de_joueurs) > 0 and i != len(self.liste_de_joueurs):
            if self.liste_de_joueurs[0].numero_ine in self.liste_de_joueurs[i].liste_d_adversaire:
                i += 1
            else :
                match = (self.liste_de_joueurs[0], self.liste_de_joueurs[i])
                liste_des_matchs.append(match)
                self.liste_de_joueurs[0].liste_d_adversaire.append(self.liste_de_joueurs[i].numero_ine)
                self.liste_de_joueurs[i].liste_d_adversaire.append(self.liste_de_joueurs[0].numero_ine)
                del self.liste_de_joueurs[i]
                del self.liste_de_joueurs[0]
                i = 1
        self.liste_de_matches = liste_des_matchs
        return liste_des_matchs

    

def main():

    fichier_joueurs = "joueurs.json"
    with open(fichier_joueurs, "r") as f:
        donnees_joueurs = json.load(f)

        liste_joueurs = []
        for cle, valeurs in donnees_joueurs.items():
            nom = valeurs.get("nom")
            prenom = valeurs.get("prenom")
            date_de_naissance = valeurs.get("date de naissance")
            numero_ine = valeurs.get("numero ine")
            gagnant_match = valeurs.get("gagnant_match")
            nombre_de_points = valeurs.get("nombre_de_points")

            joueur = Joueur(nom, prenom, date_de_naissance, numero_ine, gagnant_match, nombre_de_points)
            liste_joueurs.append(joueur)

    premier_tournoi = Tournoi("tournoi test", "Metz", "01/12/2024", "06/12/2024", "0", liste_joueurs, "sais pas", "rien")

    tour_en_cours = Tour(liste_joueurs)
    premier_tournoi.tour_actuel = tour_en_cours.tour_actuel
    tour_en_cours.randomiseur_tour1()
    liste_pour_match = []
    liste_pour_match = tour_en_cours.association_joueurs()
    resultat = []
    for joueurs_match in liste_pour_match:
        matchs = Match(joueurs_match)
        # definir ici les gagants des matchs via Vue
        resultat.append(matchs.ajouter_score())






main()



        







