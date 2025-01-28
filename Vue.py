import datetime
import re


def clear_terminal():
    print("\033[2J", end="")
    print(f"\033[{6};{0}H", end="")


def verification_input(question, condition_validite):
    reponse = input(question)
    if condition_validite(reponse):
        return reponse
    else:
        print("Saisit invalide. Veuillez réessayer.")
        return verification_input(question, condition_validite)


def verification_date(date_str):
    # Vérification si la date est au format JJ/MM/AAAA
    try:
        jour, mois, annee = map(int, date_str.split('/'))
        datetime.date(annee, mois, jour)
        return True

    except ValueError:
        return False


def affichage_simple(affichage_mot):
    print(affichage_mot)


def quitter():
    while True:
        choix = input("Voulez vous quitter l'application?\nOui\nNon\n")
        if re.match(r"^OUI$", choix, re.I):
            return True
        if re.match(r"^NON$", choix, re.I):
            return False
        else:
            "Choix non valider, entrée oui ou non\n"


def choix_gagants(joueurs_match):
    while True:
        nom1 = joueurs_match[0].nom
        prenom1 = joueurs_match[0].prenom
        ine1 = joueurs_match[0].numero_ine
        nom2 = joueurs_match[1].nom
        prenom2 = joueurs_match[1].prenom
        ine2 = joueurs_match[1].numero_ine
        print("Séléctionnez le gagnant du match:")
        print(f"Pour {nom1} {prenom1} numero INE: {ine1} Gagnant entrée 1")
        print(f"Pour {nom2} {prenom2} numero INE: {ine2} gagant, entrée 2")
        print("Pour un match nul, entrée 3:")

        choix = input("\n - ")
        if choix == "1":
            return choix
        if choix == "2":
            return choix
        if choix == "3":
            return choix
        else:
            print("Choix invalide, Réessayer.")


def nouveau_tournoi():
    nom_tournoi = verification_input("Veuillez saisir le nom du tournoi:\n - ", lambda nom_tournoi: nom_tournoi != "")
    print("Veuillez saisir le lieu du tournoi:")
    lieu_tournoi = verification_input(" - ", lambda lieu_tournoi: lieu_tournoi != "")
    print("Veuillez saisir la date de début du tournoi:")
    date_debut_tournoi = verification_input("date au format JJ/MM/AAAA\n - ", verification_date)
    print("Veuillez saisir la date de fin du tournoi:")
    date_fin_tournoi = verification_input("date au format JJ/MM/AAAA\n - ", verification_date)
    choix_remarque = input("Voulez vous ajouter une remarque pour ce tournoi?\nSaisisez Oui ou Non\n")
    if choix_remarque == "oui":
        remarques = []
        print("Pour allez à la ligne pressez une fois \"Entrée\".\nPour quitter, presser deux fois \"Entrée\".")
        while True:
            remarque = input("\nIndiquez une remarque concernant ce tournoi:\n - ")
            if remarque == "":
                break
            remarques.append(remarque)
    else:
        remarques = ["Aucune remarque"]

    print("Le nombre de tour pour le tournoi est par defaut de 4.")
    choix_nombre_tour = input("Voulez vous changer le nombre de tour?\nSaisisez Oui ou Non\n - ")
    if choix_nombre_tour == "oui":
        nombre_de_tour_str = input("Veuillez saisir le nombre de tour pour ce tournoi:\n - ")
        nombre_de_tour = int(nombre_de_tour_str)
    else:
        nombre_de_tour = 4
    infos_tournoi = (nom_tournoi, lieu_tournoi, date_debut_tournoi, date_fin_tournoi, remarques, nombre_de_tour)
    return infos_tournoi


def nouveau_joueur(settings):
    print("Veuillez saisir le Numero INE du joueur.")
    print("Au format AB suivi de 5 nombres:")
    numero_ine = verification_input(" - ", lambda numero_ine: re.match(r"^AB\d{5}$", numero_ine))
    if numero_ine in settings:
        print(f"le numero INE {numero_ine} est déja présent dans la base de données.")
        return None
    nom = verification_input("Veuillez saisir le Nom du joueur:\n - ", lambda nom: nom != "")
    prenom = verification_input("Veuillez saisir le Prénom du joueur:\n - ", lambda prenom: prenom != "")
    print("Veuillez saisir la Date de Naissance du joueur:")
    date_de_naissance = verification_input("(date au format JJ/MM/AAAA)\n - ", verification_date)
    infos_joueur = (nom, prenom, date_de_naissance, numero_ine)
    return infos_joueur


def recherche_joueur(tournoi, donnees_joueur, numero_ine):
    joueur = []
    while True:
        print(f"Veuillez saisir le Numero INE du joueur à ajouter au tournoi {tournoi.nom}.")
        print("Au format suivant: AB suivi de 5 nombres")
        print("Ou entrée 0 pour quitter:")
        joueur_ine = verification_input(" - ", lambda joueur_ine: re.match(r"^(AB\d{5}|0)$", joueur_ine))
        if joueur_ine in numero_ine:
            print(f"\nLe joueurs {joueur_ine} est déja inscrit au tournoi.")
        if joueur_ine in donnees_joueur:
            print("\nLe joueur est à présent inscrit au tournoi.")
            joueur.append(joueur_ine)
            continue
        if joueur_ine == "0":
            if len(joueur) != 0:
                return joueur
            else:
                return None
        else:
            print("\nAucun joueur correspondant n'a été trouvé.\n")


def affichage_round(tournoi, liste_de_match, date_heure_debut):
    clear_terminal()
    affichage_round = f"Voici la liste des matchs pour le Round {tournoi.tour_actuel} {date_heure_debut}:\n"
    for match in liste_de_match:
        prenom1 = match[0].prenom
        nom1 = match[0].nom
        ine1 = match[0].numero_ine
        prenom2 = match[1].prenom
        nom2 = match[1].nom
        ine2 = match[1].numero_ine

        affichage_round += f"\n{prenom1} {nom1} INE {ine1} - contre - {prenom2} {nom2} INE {ine2}\n"
    print(affichage_round)
    input("\nPressez \"Entrée\" pour terminer le Round et definir les gagnants.\n")


def affichage_resultat_match(tournoi, resultat, date_heure_fin, non_joueur):
    clear_terminal()
    affichage = f"Le Round {tournoi.tour_actuel} est fini.\nVoici les resultats des matchs {date_heure_fin}:\n"
    for resultat_round in resultat:
        for liste in tournoi.liste_des_joueurs:
            if resultat_round[0][0] in liste.numero_ine:
                prenom1 = liste.prenom
                nom1 = liste.nom
                ine1 = resultat_round[0][0]
                score1 = resultat_round[0][1]
            if resultat_round[1][0] in liste.numero_ine:
                prenom2 = liste.prenom
                nom2 = liste.nom
                ine2 = resultat_round[1][0]
                score2 = resultat_round[1][1]

        affichage += f"\n{prenom1} {nom1} - {ine1} score: {score1} contre {prenom2} {nom2} - {ine2} score: {score2}\n"

    if non_joueur != 0:
        prenom = non_joueur.prenom
        nom = non_joueur.nom
        ine = non_joueur.numero_ine
        affichage += "\nLe nombre de participant étant impaire:"
        affichage += f"Le joueurs {prenom} {nom} - numero INE: {ine} n'a pas joué ce Round."
    print(affichage)
    input("\nPressez \"Entrée\" pour continuer.\n")


def recherche_tournoi(liste_tournois):
    if liste_tournois is not None and len(liste_tournois) != 0:
        print("Voici les tournois disponible:\n")
        nombre_tournoi = len(liste_tournois)
        i = 1
        for liste in liste_tournois:
            print(f"{i} -> {liste}")
            i += 1

        while True:
            try:
                choix = int(input("\nEntrez le numero du fichier à sélectionner ou 0 pour quitter:\n - "))
                if choix == 0:
                    return None

                elif 1 <= choix <= len(liste):
                    choix -= 1
                    fichier_tournoi = liste_tournois[choix]
                    return fichier_tournoi

                else:
                    print(f"Choix invalide, veuillez entrée un nombre compris entre 0 et {nombre_tournoi}")

            except ValueError:
                print("Saisit invalide, veuillez entrée un nombre.")
            except IndexError:
                print(f"saisit invalide, veuillez saisir un nombre compris entre 0 et {i - 1}.")
    else:
        print("Il n'y a aucun tournoi de disponible, veuillez en crée un.")


def affichage_resumer(tournoi):
    print(f"\nVoici le resumer du tournoi {tournoi.nom} de {tournoi.lieu}:\n")
    print(f"Nombre de tours: {tournoi.nombre_de_tours}\n")
    print(f"Round effectués: {tournoi.tour_actuel}\n")
    print("Liste des joueurs inscrit au tournoi:")
    liste_triee = sorted(tournoi.liste_des_joueurs, key=lambda joueur: joueur.nom)
    for affichage_liste in liste_triee:
        print(affichage_liste)
    print("\nRemarque du directeur du tournoi:")
    for remarque in tournoi.remarque:
        print(remarque)
    if tournoi.tour_actuel >= 1:
        print("\nVoici le résumer des Rounds du tournois:\n")
        for round in tournoi.liste_des_tours["round"]:
            print(f"\n{round}")
            for match in tournoi.liste_des_tours["round"][round]:
                print(f"Joueur INE {match[0][0]} - {match[0][1]} contre joueur INE {match[1][0]} - {match[1][1]}")
    input("\nPressez \"Entrée\" pour quitter le résumer")


def choix_resume():
    print("\nAffichage des rapports:\n")
    print("Choisissez une option:")
    print("1. Pour la liste de tous les joueurs")
    print("2. Pour la liste de tous les tournois")
    choix = input("0. Pour revenir au Menu:\n - ")
    while True:
        if choix == "1":
            return choix
        if choix == "2":
            return choix
        if choix == "0":
            return choix
        else:
            print("Choix invalide, veuillez entrée un nombre compris entre 0 et 3")


def tour_tournoi_max():
    print("Le nombre de Round maximum pour ce tournoi a été atteind.")
    print("Ce tournoi est donc terminer.")
    print("Voici le rapport de fin de tounroi:")


def fin_tournoi():
    print("Le nombre de match possible sans rencontré deux fois le même advérsaire a été atteint.")
    print("Ce tournoi est donc terminer.")
    print("Vous pouvez consulter le rapport de fin de tounroi:")


def menu():
    while True:

        print("\n\nMenu\nchoisissez une option:")
        print("1. Création d'un nouveau joueur")
        print("2. Création d'un nouveau tournoi")
        print("3. Ajoute un joueur au tournoi:")
        print("4. Lancer / reprendre le tournoi")
        print("5. Afficher le resumer des données")
        print("0. Quitter l'applicaiton")

        choix = input("Saisir 1, 2, 3, 4, 5 ou 0:\n - ")

        if choix == "1":
            clear_terminal()
            print("Création d'un nouveau joueur:\n")
            return choix

        if choix == "2":
            clear_terminal()
            print("Création d'un nouveau tournoi:\n")
            return choix

        if choix == "3":
            clear_terminal()
            print("Ajout d'un joueur à un tournoi:\n")
            return choix

        if choix == "4":
            clear_terminal()
            print("Lancement / reprise d'un tournoi:\n")
            return choix

        if choix == "5":
            clear_terminal()
            print("Résumer des données:\n")
            return choix

        if choix == "0":
            clear_terminal()
            return choix

        else:
            print("\nChoix invalide, Réessayer.")
