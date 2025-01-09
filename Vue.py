import datetime
import re
import json


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
        return True
    
    except ValueError:
        return False


def quitter():
    clear_terminal()
    while True:
        choix = input("Voulez vous quitter l'application?\nOui\nNon\n")
        if choix == "oui":
            return True
        if choix == "non":
            return False
        else:
            "Choix non valider, entrée oui ou non\n"



def choix_gagants(joueurs_match, infos_joueurs):
    clear_terminal()
    while True:
        prenom_joueur1 = infos_joueurs[joueurs_match[0].numero_ine]["prenom"]
        nom_joueus1 = infos_joueurs[joueurs_match[0].numero_ine]["nom"]
        prenom_jouers2 = infos_joueurs[joueurs_match[1].numero_ine]["prenom"]
        nom_jouer2 = infos_joueurs[joueurs_match[1].numero_ine]["nom"]
        texte = (f"Séléctionnez le gagnant du match:\nPour {prenom_joueur1} {nom_joueus1} numero INE: {joueurs_match[0].numero_ine} Gagnant entrée 1\nPour {prenom_jouers2} {nom_jouer2} numero INE: {joueurs_match[1].numero_ine} gagant, entrée 2\nPour un match nul, entrée 3:\n")
        print(texte)
        choix = input("- ")
        if choix == "1":
            return choix
        if choix == "2":
            return choix
        if choix == "3":
            return choix
        else:
            print("Choix invalide, Réessayer.")


def nouveau_tournoi():
    clear_terminal()
    nom_tournoi = verification_input("Veuillez saisir le nom du tournoi:\n", lambda nom_tournoi: nom_tournoi != "")
    lieu_tournoi = verification_input("Veuillez saisir le lieu du tournoi:\n", lambda lieu_tournoi: lieu_tournoi != "")
    date_debut_tournoi = verification_input("Veuillez saisir la date de début du tournoi:\n(date au format JJ/MM/AAAA)\n", verification_date)
    date_fin_tournoi = verification_input("Veuillez saisir la date de fin du tournoi:\n(date au format JJ/MM/AAAA)\n", verification_date)
    choix_remarque = input("Voulez vous ajouter une remarque pour ce tournoi?\nSaisisez Oui ou Non\n")
    if choix_remarque == "oui":
        remarque = input("Indiquez les remarques concernant ce tournoi:\n")
    else:
        remarque = " "

    choix_nombre_tour = input ("Le nombre de tour pour le tournoi est par defaut de 4.\nVoulez vous changer le nombre de tour?\nSaisisez Oui ou Non\n")
    if choix_nombre_tour == "oui":
        nombre_de_tour_str = input("Veuillez saisir le nombre de tour pour ce tournoi:\n")
        nombre_de_tour = int(nombre_de_tour_str)
    else:
        nombre_de_tour = 4
    infos_tournoi = (nom_tournoi, lieu_tournoi, date_debut_tournoi, date_fin_tournoi, remarque, nombre_de_tour)
    return infos_tournoi


def nouveau_joueur():
    clear_terminal()
    numero_ine = verification_input("Veuillez saisir le Numero INE du joueur.\nAu format AB suivi de 5 nombres:\n", lambda numero_ine: r"^(AB)\d{5}$")
    nom = verification_input("Veuillez saisir le Nom du joueur:\n", lambda nom: nom != "")
    prenom = verification_input("Veuillez saisir le Prénom du joueur:\n", lambda prenom: prenom != "")
    date_de_naissance = verification_input("Veuillez saisir la Date de Naissance du joueur:\n(date au format JJ/MM/AAAA)\n", verification_date())

    infos_joueur = (nom, prenom, date_de_naissance, numero_ine)
    return infos_joueur


def recherche_joueur(joueurs):
    clear_terminal()
    joueur_ine = verification_input("Veuillez saisir le Numero INE du joueur à rechercher.\nAu format AB suivi de 5 nombres:\n", lambda joueur_ine: r"^(AB)\d{5}$")
    if joueur_ine in joueurs:
        print("\nLe joueur est présent dans la base de données des joueurs\n")
        return joueur_ine
    else:
        print("\nAucun joueur correspondant n'a été trouvé.\n")


def affichage_round(tournoi, liste_de_match, infos_joueurs):
    clear_terminal()

    affichage_round = f"Voici la liste des matchs pour le Round {tournoi.tour_actuel[0]}:\n"
    for match in liste_de_match:
        prenom_joueur1 = infos_joueurs[match[0].numero_ine]["prenom"]
        nom_joueus1 = infos_joueurs[match[0].numero_ine]["nom"]
        prenom_jouers2 = infos_joueurs[match[1].numero_ine]["prenom"]
        nom_jouer2 = infos_joueurs[match[1].numero_ine]["nom"]
        affichage_round += f"{prenom_joueur1} {nom_joueus1} - {match[0].numero_ine} contre {prenom_jouers2} {nom_jouer2} - {match[1].numero_ine}\n" 
    print(affichage_round)
    input("Pressez \"Entrée\" pour terminer le Round\n")


def affichage_resultat_match(tournoi, resultat, infos_joueurs, non_joueur):
    clear_terminal()
    affichage_resultat = f"Le Round {tournoi.tour_actuel} en fini.\nvoici le resultat des matchs:\n"
    for resultat_round in resultat:
        prenom_joueur1 = infos_joueurs[resultat_round[0][0]]["prenom"]
        nom_joueus1 = infos_joueurs[resultat_round[0][0]]["nom"]
        prenom_jouers2 = infos_joueurs[resultat_round[1][0]]["prenom"]
        nom_jouer2 = infos_joueurs[resultat_round[1][0]]["nom"]

        affichage_resultat += f"{prenom_joueur1} {nom_joueus1} - {resultat_round[0][0]} score: {resultat_round[0][1]} contre {prenom_jouers2} {nom_jouer2} - {resultat_round[1][0]} score: {resultat_round[1][1]}\n" 
    if non_joueur != 0:
        prenom_non_joueur = infos_joueurs[non_joueur.numero_ine]["prenom"]
        nom_non_joueur = infos_joueurs[non_joueur.numero_ine]["nom"]
        affichage_resultat += f"le nombre de participant étant impaire, le joueurs {prenom_non_joueur} {nom_non_joueur} - numero INE: {non_joueur.numero_ine} n'a pas joué ce Round."
    print(affichage_resultat)
    input("Pressez \"Entrée\" pour continuer\n")


def recherche_tournoi():
    clear_terminal()
    choix = input("Voici les tournois disponible:\n entrez le numero du fichier à sélectionner ou 0 pour quitter:")
    return choix


def tournoi_en_cours():
    clear_terminal()
    nom_tournoi = verification_input("Veuillez saisir le nom du tournoi:\n", lambda nom_tournoi: nom_tournoi != "")
    lieu_tournoi = verification_input("Veuillez saisir le lieu du tournoi:\n", lambda lieu_tournoi: lieu_tournoi != "")
    date_debut_tournoi = verification_input("Veuillez saisir la date de début du tournoi:\n(date au format JJ/MM/AAAA)\n", verification_date)
    date_debut = date_debut_tournoi.replace("/", "")
    infos_tournoi = (nom_tournoi, lieu_tournoi, date_debut)
    return infos_tournoi


def fin_du_tournoi():
    pass


def menu():
    while True:
        
        print("\n\nMenu\nchoisissez une option:\n1. Création d'un nouveau joueur\n2. Création d'un nouveau tournoi\n3. Ajoute un joueur au tournoi:\n4. Lancer / reprendre le tournoi\n5. Quitter l'applicaiton du tournoi")
        choix = input("Saisir 1, 2, 3, 4 ou 5:\n")
        
        if choix == "1":
            print("Création d'un nouveau joueur:\n")
            return choix
        
        if choix == "2":
            print("Création d'un nouveau tournoi:\n")
            return choix
        
        if choix == "3":
            print("Ajoute un joueur au tournoi:\n")
            return choix

        if choix == "4":
            print("Lancement / reprise d'un tournoi:\n")
            return choix

        if choix == "5":
            return choix

        else:
            print("Choix invalide, Réessayer.")

        
