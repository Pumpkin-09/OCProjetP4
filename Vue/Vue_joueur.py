import re
from Vue.Vue_verification import AffichageVerification

class AffichageJoueur:

    @staticmethod
    def nouveau_joueur(settings):
        print("Veuillez saisir le Numéro INE du joueur.")
        print("Au format AB suivi de 5 nombres:")
        numero_ine = AffichageVerification.verification_input(" - ", lambda numero_ine: re.match(r"^AB\d{5}$", numero_ine))
        if numero_ine in settings:
            print(f"le numéro INE {numero_ine} est déjà présent dans la base de données.")
            return None
        nom = AffichageVerification.verification_input("Veuillez saisir le Nom du joueur:\n - ", lambda nom: nom != "")
        prenom = AffichageVerification.verification_input("Veuillez saisir le Prénom du joueur:\n - ", lambda prenom: prenom != "")
        print("Veuillez saisir la Date de Naissance du joueur:")
        date_de_naissance = AffichageVerification.verification_input("(date au format JJ/MM/AAAA)\n - ", AffichageVerification.verification_date)
        infos_joueur = (nom, prenom, date_de_naissance, numero_ine)
        return infos_joueur

    @staticmethod
    def recherche_joueur(tournoi, donnees_joueur, numero_ine):
        joueur = []
        while True:
            print(f"Veuillez saisir le Numéro INE du joueur à ajouter au tournoi {tournoi.nom}.")
            print("au format suivant: AB suivi de 5 nombres")
            print("ou entrez 0 pour quitter:")
            joueur_ine = AffichageVerification.verification_input(" - ", lambda joueur_ine: re.match(r"^(AB\d{5}|0)$", joueur_ine))
            if joueur_ine in numero_ine or joueur_ine in joueur:
                print(f"Le joueur {joueur_ine} est déjà inscrit au tournoi.\n\n")
                continue
            if joueur_ine in donnees_joueur and joueur_ine not in joueur:
                print("Le joueur est à présent inscrit au tournoi.\n\n")
                joueur.append(joueur_ine)
                continue
            if joueur_ine == "0":
                if len(joueur) != 0:
                    return joueur
                else:
                    return None
            else:
                print("\nAucun joueur correspondant n'a été trouvé.\n")