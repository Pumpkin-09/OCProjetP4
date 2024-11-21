from datetime import date



class Joueur:

    def __init__(self, nom_de_famille, prenom, date_de_naissance, numero_ine, nombre_de_points):
            
        self.nom_de_famille = nom_de_famille
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.numero_ine = numero_ine
        self.nombre_de_points = nombre_de_points = 0.0


class Tournoi:

    def __init__(self, nom, lieu, date_de_debut, date_de_fin, nombre_de_tours, tour_actuel, liste_des_tours, liste_des_joueurs, remarque):
     
        self.nom = nom
        self.lieu = lieu
        self.date_de_debut = date_de_debut = date
        self.date_de_fin = date_de_fin = date
        self.nombre_de_tours = nombre_de_tours = 4
        self.tour_actuel = tour_actuel
        self.liste_des_tours = liste_des_tours
        self.liste_des_joueurs = liste_des_joueurs
        self.remarque = remarque


class Match:

    def __init__(self, joueur_1, joueur_2, score_1, score_2):

        self.joueur_1 = joueur_1
        self.joueur_2 = joueur_2
        self.score_1 = score_1 = 0
        self.score_2 = score_2 = 0


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


class Tours:

    def __init__ (self, numero_du_tour, match):

        self.numero_du_tour = numero_du_tour
        self.match = match






