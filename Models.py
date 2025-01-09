import random



class Joueur:

    def __init__(self, numero_ine, score=0.0):
        self.numero_ine = numero_ine
        self.score = score


class Tournoi:

    def __init__(self, nom, lieu, date_de_debut, date_de_fin, remarque, nombre_de_tours=4, tour_actuel=0, liste_des_joueurs=[], liste_des_tours={"round":{}, "adversaire":[]}):
        self.nom = nom
        self.lieu = lieu
        self.date_de_debut = date_de_debut
        self.date_de_fin = date_de_fin
        self.remarque = remarque
        self.nombre_de_tours = nombre_de_tours
        self.tour_actuel = tour_actuel
        self.liste_des_joueurs = liste_des_joueurs
        self.liste_des_tours = liste_des_tours


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
            self.joueur_2.score +=1
            score_1 = 0
            score_2 = 1
        
        else: # match nul
            self.joueur_1.score += 0.5
            self.joueur_2.score += 0.5
            score_1 = 0.5
            score_2 = 0.5

        resultat = ([self.joueur_1.numero_ine, score_1], [self.joueur_2.numero_ine, score_2])
        return tuple(resultat)


class Tour:

    def __init__ (self, liste_des_joueurs):
        self.liste_des_joueurs = liste_des_joueurs
    
    def randomiseur_tour1(self):
        random.shuffle(self.liste_des_joueurs)
        
    def triage_par_points(self):
        self.liste_des_joueurs.sort(key=lambda item: item.score, reverse=True)

    def association_joueurs(self, tournoi): # rajouter le cas ou tout les match on deja ete jouer!
        liste_travail = self.liste_des_joueurs.copy()
        if len(liste_travail)%2 != 0:
            impair = random.randint(0, len(liste_travail)-1)
            del liste_travail[impair]
        i = 1
        liste_de_matchs = []
        while len(liste_travail) > 0 and i != len(liste_travail):
            if (liste_travail[0].numero_ine, liste_travail[i].numero_ine) or (liste_travail[i].numero_ine, liste_travail[0].numero_ine) in tournoi.liste_des_tours["adversaire"]:
                i += 1
            else :
                match = (liste_travail[0], liste_travail[i])
                liste_de_matchs.append(match)
                tournoi.liste_des_tours["adversaire"].extend(liste_de_matchs[0].numero_ine, liste_de_matchs[i].numero_ine)
                del liste_travail[i]
                del liste_travail[0]
                i = 1
        return liste_de_matchs
