from Controleur.Controleur_joueur import ControleJoueur
from Controleur.Controleur_tournoi import ControleTournoi, ExecutionTournoi, DonneesTournoi
from Controleur.Controleur_rapport import Rapport
from Vue.Vue_tournoi import AffichageTournoi
from Vue.Vue_round import AffichageRound
from Vue.Vue_menu import AffichageMenu


class MenuControleur:

    def __init__(self):
        self.donnees_joueur = ControleJoueur.donnees_joueurs()

    def main_menu(self):
        tournoi = None
        while True:
            choix_menu = AffichageMenu.menu()
            if choix_menu == "1":  # ajout d'un joueur a la base de donnees des joueurs
                ControleJoueur.creation_joueur()
                self.donnees_joueur = ControleJoueur.donnees_joueurs()

            if choix_menu == "2":  # creation d'un nouveau tournoi
                ControleTournoi.creation_tournoi()

            if choix_menu == "3":  # Ajoute un joueur au tournoi
                tournoi = None
                controle_tournoi = ControleTournoi(self.donnees_joueur)
                liste = DonneesTournoi.liste_des_tournois()
                tournoi = controle_tournoi.recuperation_donnees_tournoi(AffichageTournoi.recherche_tournoi(liste))
                if tournoi is None:
                    continue
                ControleJoueur.ajout_joueur_tournoi(tournoi)
                # tournoi.sauvegard()

            if choix_menu == "4":  # lancement du tournoi
                liste_tournois = DonneesTournoi.liste_des_tournois()
                if len(liste_tournois) == 0:
                    mot_affichage = "Aucun tournoi enregistrer, veuiller en créer un:"
                    AffichageRound.affichage_simple(mot_affichage)
                    ControleTournoi.creation_tournoi()
                elif len(liste_tournois) != 0:
                    choix_tournoi = AffichageTournoi.recherche_tournoi(liste_tournois)
                    if choix_tournoi is None:
                        continue
                    controle_tournoi = ControleTournoi(self.donnees_joueur)
                    tournoi = controle_tournoi.recuperation_donnees_tournoi(choix_tournoi)
                    if len(tournoi.liste_des_joueurs) <= 1:
                        mot = "\nMoins de deux joueurs sont inscrits à ce tournoi, Veuillez en selectionner.\n"
                        AffichageRound.affichage_simple(mot)
                        non = ControleJoueur.ajout_joueur_tournoi(tournoi)
                        if non is None:
                            continue
                        tournoi.sauvegard()
                    if tournoi.tour_actuel == 0:
                        ExecutionTournoi.demarer_tournoi(tournoi)
                    if tournoi.tour_actuel != tournoi.nombre_de_tours:
                        AffichageRound.affichage_resumer(tournoi)
                        ExecutionTournoi.continuer_tournoi(tournoi)
                    if tournoi.tour_actuel == tournoi.nombre_de_tours:
                        AffichageTournoi.tour_tournoi_max()
                        AffichageRound.affichage_resumer(tournoi)
                        tournoi = None

            if choix_menu == "5":  # affiche le resume du tournoi choisi
                liste_tournois = DonneesTournoi.liste_des_tournois()
                choix_resume = AffichageMenu.choix_resume()
                rapport = Rapport(choix_resume, liste_tournois, self.donnees_joueur)
                rapport.resume_donnees()

            if choix_menu == "0":  # fin de l'application
                if tournoi is not None:
                    tournoi.sauvegard()
                affichage_mot = ("Au revoir")
                AffichageRound.affichage_simple(affichage_mot)
                return


if __name__ == "__main__":
    menu = MenuControleur.main_menu()
