import re
from Vue.Vue_verification import AffichageVerification

class AffichageMenu:

    @staticmethod
    def choix_resume():
        while True:
            print("\nAffichage des rapports:\n")
            print("Choisissez une option:")
            print("1. Pour la liste de tous les joueurs")
            print("2. Pour la liste de tous les tournois")
            choix = input("0. Pour revenir au Menu:\n - ")
            if choix == "1":
                return choix
            if choix == "2":
                return choix
            if choix == "0":
                return choix
            else:
                print("Choix invalide, veuillez entrer un nombre compris entre 0 et 2")

    @staticmethod
    def menu():
        while True:

            print("\n\n--------------Menu--------------")
            print("     Choisissez une option:")
            print("1. Création d'un nouveau joueur")
            print("2. Création d'un nouveau tournoi")
            print("3. Ajout d'un joueur au tournoi:")
            print("4. Lancer / reprendre le tournoi")
            print("5. Afficher le resumé des données")
            print("0. Quitter l'applicaiton")
            print("---------------------------------")

            choix = input("Saisir 1, 2, 3, 4, 5 ou 0:\n - ")

            if choix == "1":
                AffichageVerification.clear_terminal()
                print("Création d'un nouveau joueur:\n")
                return choix

            if choix == "2":
                AffichageVerification.clear_terminal()
                print("Création d'un nouveau tournoi:\n")
                return choix

            if choix == "3":
                AffichageVerification.clear_terminal()
                print("Ajout d'un joueur à un tournoi:\n")
                return choix

            if choix == "4":
                AffichageVerification.clear_terminal()
                print("Lancement / reprise d'un tournoi:\n")
                return choix

            if choix == "5":
                AffichageVerification.clear_terminal()
                print("Résumé des données:\n")
                return choix

            if choix == "0":
                AffichageVerification.clear_terminal()
                return choix

            else:
                print("\nChoix invalide, Réessayez.")

    @staticmethod
    def quitter():
        while True:
            choix = input("Voulez-vous quitter l'application?\nOui\nNon\n")
            if re.match(r"^OUI$", choix, re.I):
                return True
            if re.match(r"^NON$", choix, re.I):
                return False
            else:
                "Choix non valide, entrez oui ou non\n"