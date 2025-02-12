from Vue.Vue_round import AffichageRound
from Vue.Vue_tournoi import AffichageTournoi
from Models.Models_donnees import Joueur
from Controleur.Controleur_tournoi import ControleTournoi


class Rapport:
    def __init__(self, choix_resume, liste_des_tournois, donnees_joueurs):
        self.choix = choix_resume
        self.liste_des_tournois = liste_des_tournois
        self.donnees_joueurs = donnees_joueurs

    def resume_donnees(self):
        while True:
            if self.choix == "1":
                liste_joueurs = []
                if self.donnees_joueurs is None:
                    affichage_mot = "\nPas de joueur enregistré."
                    AffichageRound.affichage_simple(affichage_mot)
                    break

                if len(self.donnees_joueurs) == 0:
                    affichage_mot = "\nPas de joueur enregistré."
                    AffichageRound.affichage_simple(affichage_mot)
                    break

                for ine_joueurs, donnees_joueur in self.donnees_joueurs.items():
                    joueur = Joueur(donnees_joueur["numero ine"], donnees_joueur["nom"],
                                    donnees_joueur["prenom"], donnees_joueur["date de naissance"])

                    liste_joueurs.append(joueur)
                liste_triee = sorted(liste_joueurs, key=lambda joueur: joueur.nom)
                affichage_mot = "\n----------------------------------------"
                AffichageRound.affichage_simple(affichage_mot)
                affichage_mot = "\nVoici la liste de tous les joueurs:"
                AffichageRound.affichage_simple(affichage_mot)
                for affichage in liste_triee:
                    AffichageRound.affichage_simple(affichage)
                break

            if self.choix == "2":
                if self.liste_des_tournois is None:
                    break
                choix_tournoi = AffichageTournoi.recherche_tournoi(self.liste_des_tournois)
                if choix_tournoi is None:
                    break
                controle_tournoi = ControleTournoi(self.donnees_joueurs)
                tournoi = controle_tournoi.recuperation_donnees_tournoi(choix_tournoi)
                AffichageRound.affichage_resumer(tournoi)
            else:
                return
