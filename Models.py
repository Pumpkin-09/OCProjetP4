from dataclasses import dataclass, field
from datetime import date

@dataclass
class Joueur:
    nom_de_famille: str
    prenom: str
    date_de_naissance: date
    numero_ine: str
    nombre_de_points: float = 0






@dataclass
class Tournoi:
    nom: str
    lieu: str
    date_de_debut: date
    date_de_fin: date
    nombre_de_tours: int = 4
    tour_actuel: str
    liste_des_tours: str
    liste_joueurs: str
    remarque: str


@dataclass
class Match:
    joueur_1: Joueur
    joueur_2: Joueur
    score_1: int = 0
    score_2: int = 0

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




@dataclass
class Tours:

    numero_du_tours: str
    matchs: Match[str] = field(default_factory=list)






