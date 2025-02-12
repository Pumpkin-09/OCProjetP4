import random


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
                    historique = tournoi.liste_des_tours["adversaire"]
                    if liste1 in historique or liste2 in historique:
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
