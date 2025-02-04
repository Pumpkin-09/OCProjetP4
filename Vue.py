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
        print("Saisie invalide. Veuillez réessayer.")
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
        choix = input("Voulez-vous quitter l'application?\nOui\nNon\n")
        if re.match(r"^OUI$", choix, re.I):
            return True
        if re.match(r"^NON$", choix, re.I):
            return False
        else:
            "Choix non valide, entrez oui ou non\n"


def choix_gagants(joueurs_match):
    while True:
        nom1 = joueurs_match[0].nom
        prenom1 = joueurs_match[0].prenom
        ine1 = joueurs_match[0].numero_ine
        nom2 = joueurs_match[1].nom
        prenom2 = joueurs_match[1].prenom
        ine2 = joueurs_match[1].numero_ine
        print("Sélectionnez le gagnant du match:")
        print(f"Pour {nom1} {prenom1} numéro INE: {ine1} gagnant, entrez 1")
        print(f"Pour {nom2} {prenom2} numéro INE: {ine2} gagnant, entrez 2")
        print("Pour un match nul, entrez 3:")

        choix = input("\n - ")
        if choix == "1":
            return choix
        if choix == "2":
            return choix
        if choix == "3":
            return choix
        else:
            print("Choix invalide, Réessayez.")


def nouveau_tournoi():
    nom_tournoi = verification_input("Veuillez saisir le nom du tournoi:\n - ", lambda nom_tournoi: nom_tournoi != "")
    print("Veuillez saisir le lieu du tournoi:")
    lieu_tournoi = verification_input(" - ", lambda lieu_tournoi: lieu_tournoi != "")
    print("Veuillez saisir la date de début du tournoi:")
    date_debut_tournoi = verification_input("date au format JJ/MM/AAAA\n - ", verification_date)
    print("Veuillez saisir la date de fin du tournoi:")
    date_fin_tournoi = verification_input("date au format JJ/MM/AAAA\n - ", verification_date)
    choix_remarque = input("Voulez-vous ajouter une remarque pour ce tournoi?\nSaisissez Oui ou Non\n")
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

    print("Le nombre de tours pour le tournoi est par défaut de 4.")
    choix_nombre_tour = input("Voulez-vous changer le nombre de tours?\nSaisissez Oui ou Non\n - ")
    if choix_nombre_tour == "oui":
        nombre_de_tour_str = input("Veuillez saisir le nombre de tours pour ce tournoi:\n - ")
        nombre_de_tour = int(nombre_de_tour_str)
    else:
        nombre_de_tour = 4
    infos_tournoi = (nom_tournoi, lieu_tournoi, date_debut_tournoi, date_fin_tournoi, remarques, nombre_de_tour)
    return infos_tournoi


def nouveau_joueur(settings):
    print("Veuillez saisir le Numéro INE du joueur.")
    print("Au format AB suivi de 5 nombres:")
    numero_ine = verification_input(" - ", lambda numero_ine: re.match(r"^AB\d{5}$", numero_ine))
    if numero_ine in settings:
        print(f"le numéro INE {numero_ine} est déjà présent dans la base de données.")
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
        print(f"Veuillez saisir le Numéro INE du joueur à ajouter au tournoi {tournoi.nom}.")
        print("au format suivant: AB suivi de 5 nombres")
        print("ou entrez 0 pour quitter:")
        joueur_ine = verification_input(" - ", lambda joueur_ine: re.match(r"^(AB\d{5}|0)$", joueur_ine))
        if joueur_ine in numero_ine:
            print(f"\nLe joueur {joueur_ine} est déjà inscrit au tournoi.")
        if joueur_ine in donnees_joueur and joueur_ine not in joueur:
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
    input("\nPressez \"Entrée\" pour terminer le Round et définir les gagnants.\n")


def affichage_resultat_match(tournoi, resultat, date_heure_fin, non_joueur):
    clear_terminal()
    affichage = f"Le Round {tournoi.tour_actuel} est fini.\nVoici les résultats des matchs {date_heure_fin}:\n"
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
        affichage += "\nLe nombre de participants étant impaire:"
        affichage += f"Le joueur {prenom} {nom} - numero INE: {ine} n'a pas joué ce Round."
    print(affichage)
    input("\nPressez \"Entrée\" pour continuer.\n")


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


def affichage_resumer(tournoi):
    print(f"\nVoici le résumé du tournoi {tournoi.nom} de {tournoi.lieu}:\n")
    print(f"Nombre de tours: {tournoi.nombre_de_tours}\n")
    print(f"Rounds effectués: {tournoi.tour_actuel}\n")
    print("Liste des joueurs inscrits au tournoi:")
    liste_triee = sorted(tournoi.liste_des_joueurs, key=lambda joueur: joueur.nom)
    for affichage_liste in liste_triee:
        print(affichage_liste)
    print("\nRemarque du directeur du tournoi:")
    for remarque in tournoi.remarque:
        print(remarque)
    if tournoi.tour_actuel >= 1:
        print("\nVoici le résumé des Rounds du tournoi:\n")
        for round in tournoi.liste_des_tours["round"]:
            print(f"\n{round}")
            for match in tournoi.liste_des_tours["round"][round]:
                print(f"Joueur INE {match[0][0]} - {match[0][1]} contre joueur INE {match[1][0]} - {match[1][1]}")
    input("\nPressez \"Entrée\" pour quitter le résumé")


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


def tour_tournoi_max():
    print("Le nombre de Rounds maximum pour ce tournoi a été atteint.")
    print("Ce tournoi est donc terminé.")
    print("Voici le rapport de fin de tounroi:")


def fin_tournoi():
    print("Le nombre de matchs possible sans rencontrer deux fois le même adversaire a été atteint.")
    print("Ce tournoi est donc terminé.")
    print("Vous pouvez consulter le rapport de fin de tounroi:")


def menu():
    while True:

        print("\n\nMenu\nChoisissez une option:")
        print("1. Création d'un nouveau joueur")
        print("2. Création d'un nouveau tournoi")
        print("3. Ajout d'un joueur au tournoi:")
        print("4. Lancer / reprendre le tournoi")
        print("5. Afficher le resumé des données")
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
            print("Résumé des données:\n")
            return choix

        if choix == "0":
            clear_terminal()
            return choix

        else:
            print("\nChoix invalide, Réessayez.")
