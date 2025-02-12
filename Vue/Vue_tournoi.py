import re
from Vue.Vue_verification import AffichageVerification


class AffichageTournoi:
    @staticmethod
    def choix_gagants(joueurs_match):
        while True:
            nom1 = joueurs_match[0].nom
            prenom1 = joueurs_match[0].prenom
            ine1 = joueurs_match[0].numero_ine
            nom2 = joueurs_match[1].nom
            prenom2 = joueurs_match[1].prenom
            ine2 = joueurs_match[1].numero_ine
            print("\nSélectionnez le gagnant du match:")
            print(f"Pour {nom1} {prenom1} numéro INE: {ine1} gagnant, entrez 1")
            print(f"Pour {nom2} {prenom2} numéro INE: {ine2} gagnant, entrez 2")
            print("Pour un match nul, entrez 3:")

            choix = input(" - ")
            if choix == "1":
                return choix
            if choix == "2":
                return choix
            if choix == "3":
                return choix
            else:
                print("Choix invalide, Réessayez.")

    @staticmethod
    def nouveau_tournoi():
        print("Veuillez saisir le nom du tournoi:")
        nom_tournoi = AffichageVerification.verification_input(" - ", lambda nom_tournoi: nom_tournoi != "")
        print("Veuillez saisir le lieu du tournoi:")
        lieu_tournoi = AffichageVerification.verification_input(" - ", lambda lieu_tournoi: lieu_tournoi != "")
        print("Veuillez saisir la date de début du tournoi:")
        print("date au format JJ/MM/AAAA")
        date_debut_tournoi = AffichageVerification.verification_input(" - ", AffichageVerification.verification_date)
        print("Veuillez saisir la date de fin du tournoi:")
        print("date au format JJ/MM/AAAA")
        date_fin_tournoi = AffichageVerification.verification_input(" - ", AffichageVerification.verification_date)
        choix_remarque = input("Voulez-vous ajouter une remarque pour ce tournoi?\nSaisissez Oui ou Non\n")
        if re.match(r"^OUI$", choix_remarque, re.I):
            remarques = []
            print("Pour allez à la ligne pressez une fois \"Entrée\".\nPour quitter, presser deux fois \"Entrée\".")
            while True:
                remarque = input("\nIndiquez une remarque concernant ce tournoi:\n - ")
                if remarque == "":
                    break
                remarques.append(remarque)
        if re.match(r"^NON$", choix_remarque, re.I):
            remarques = ["Aucune remarque"]

        print("Le nombre de tours pour le tournoi est par défaut de 4.")
        choix_nombre_tour = input("Voulez-vous changer le nombre de tours?\nSaisissez Oui ou Non\n - ")
        if re.match(r"^OUI$", choix_nombre_tour, re.I):
            nombre_de_tour_str = input("Veuillez saisir le nombre de tours pour ce tournoi:\n - ")
            nombre_de_tour = int(nombre_de_tour_str)
        if re.match(r"^NON$", choix_nombre_tour, re.I):
            nombre_de_tour = 4
        infos_tournoi = (nom_tournoi, lieu_tournoi, date_debut_tournoi, date_fin_tournoi, remarques, nombre_de_tour)
        return infos_tournoi

    @staticmethod
    def recherche_tournoi(liste_tournois):
        if liste_tournois is not None and len(liste_tournois) != 0:
            print("Voici les tournois disponibles:\n")
            nombre_tournoi = len(liste_tournois)
            i = 1
            for liste in liste_tournois:
                print(f"{i} -> {liste}")
                i += 1

            while True:
                try:
                    choix = int(input("\nEntrez le numéro du fichier à sélectionner, ou 0 pour quitter:\n - "))
                    if choix == 0:
                        return None

                    elif 1 <= choix <= len(liste):
                        choix -= 1
                        fichier_tournoi = liste_tournois[choix]
                        return fichier_tournoi

                    else:
                        print(f"Choix invalide, veuillez entrer un nombre compris entre 0 et {nombre_tournoi}")

                except ValueError:
                    print("Saisie invalide, veuillez entrer un nombre.")
                except IndexError:
                    print(f"Saisie invalide, veuillez entrer un nombre compris entre 0 et {i - 1}.")
        else:
            print("Il n'y a aucun tournoi de disponible, veuillez en créer un.")

    @staticmethod
    def tour_tournoi_max():
        print("Le nombre de Rounds maximum pour ce tournoi a été atteint.")
        print("Ce tournoi est donc terminé.")
        print("Voici le rapport de fin de tounroi:")

    @staticmethod
    def fin_tournoi():
        print("Le nombre de matchs possible sans rencontrer deux fois le même adversaire a été atteint.")
        print("Ce tournoi est donc terminé.")
        print("Vous pouvez consulter le rapport de fin de tounroi:")
