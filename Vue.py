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
    while True:
        choix = input("Voulez vous quitter l'application?\nOui\nNon\n")
        if choix == "oui":
            return True
        if choix == "non":
            return False
        else:
            "Choix non valider, entrée oui ou non\n"



def choix_gagants(joueurs_match):
    while True:
        texte = (f"Séléctionnez le gagnant du match:\nPour {joueurs_match[0].nom} {joueurs_match[0].prenom} numero INE: {joueurs_match[0].numero_ine} Gagnant entrée 1\nPour {joueurs_match[1].nom} {joueurs_match[1].prenom} numero INE: {joueurs_match[1].numero_ine} gagant, entrée 2\nPour un match nul, entrée 3:\n")
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
    nom_tournoi = verification_input("Veuillez saisir le nom du tournoi:\n", lambda nom_tournoi: nom_tournoi != "")
    lieu_tournoi = verification_input("Veuillez saisir le lieu du tournoi:\n", lambda lieu_tournoi: lieu_tournoi != "")
    date_debut_tournoi = verification_input("Veuillez saisir la date de début du tournoi:\n(date au format JJ/MM/AAAA)\n", verification_date)
    date_fin_tournoi = verification_input("Veuillez saisir la date de fin du tournoi:\n(date au format JJ/MM/AAAA)\n", verification_date)
    choix_remarque = input("Voulez vous ajouter une remarque pour ce tournoi?\nSaisisez Oui ou Non\n")
    if choix_remarque == "oui":
        remarque = input("Indiquez les remarques concernant ce tournoi:\n")
    else:
        remarque = "Aucune"

    choix_nombre_tour = input ("Le nombre de tour pour le tournoi est par defaut de 4.\nVoulez vous changer le nombre de tour?\nSaisisez Oui ou Non\n")
    if choix_nombre_tour == "oui":
        nombre_de_tour_str = input("Veuillez saisir le nombre de tour pour ce tournoi:\n")
        nombre_de_tour = int(nombre_de_tour_str)
    else:
        nombre_de_tour = 4
    infos_tournoi = (nom_tournoi, lieu_tournoi, date_debut_tournoi, date_fin_tournoi, remarque, nombre_de_tour)
    return infos_tournoi


def nouveau_joueur():
    numero_ine = verification_input("Veuillez saisir le Numero INE du joueur.\nAu format AB suivi de 5 nombres:\n", lambda numero_ine: r"^(AB)\d{5}$")
    nom = verification_input("Veuillez saisir le Nom du joueur:\n", lambda nom: nom != "")
    prenom = verification_input("Veuillez saisir le Prénom du joueur:\n", lambda prenom: prenom != "")
    date_de_naissance = verification_input("Veuillez saisir la Date de Naissance du joueur:\n(date au format JJ/MM/AAAA)\n", verification_date())
    infos_joueur = (nom, prenom, date_de_naissance, numero_ine)
    return infos_joueur


def recherche_joueur(donnees_joueur, nombre_joueur):
    joueur_ine = verification_input("Veuillez saisir le Numero INE du joueur à ajouter au tournoi.\nAu format AB suivi de 5 nombres:\n", lambda joueur_ine: r"^(AB)\d{5}$")
    if joueur_ine in donnees_joueur:
        print(f"\nLe joueur est à présent inscrit au tournoi.\nle total de joueurs est de: {nombre_joueur+1}")
        return joueur_ine
    else:
        print("\nAucun joueur correspondant n'a été trouvé.\n")


def affichage_round(tournoi, liste_de_match, date_heure_debut):
    clear_terminal()
    affichage_round = f"Voici la liste des matchs pour le Round {tournoi.tour_actuel} {date_heure_debut}:\n"
    for match in liste_de_match:
        affichage_round += f"\n{match[0].prenom} {match[0].nom} INE {match[0].numero_ine} - contre - {match[1].prenom} {match[1].nom} INE {match[1].numero_ine}\n" 
    print(affichage_round)
    input("\nPressez \"Entrée\" pour terminer le Round et definir les gagnants.\n")


def affichage_resultat_match(tournoi, liste_des_joueurs, resultat, date_heure_fin, non_joueur):
    clear_terminal()
    affichage_resultat = f"Le Round {tournoi.tour_actuel} en fini.\nvoici le resultat des matchs {date_heure_fin}:\n"
    for resultat_round in resultat:
        for liste in liste_des_joueurs:
            if resultat_round[0][0] in liste.numero_ine:
                prenom_joueur_1 = liste.prenom
                nom_joueur_1 = liste.nom
            if resultat_round[1][0] in liste.numero_ine:
                prenom_joueur_2 = liste.prenom
                nom_joueur_2 = liste.nom

        affichage_resultat += f"\n{prenom_joueur_1} {nom_joueur_1} - {resultat_round[0][0]} score: {resultat_round[0][1]} contre {prenom_joueur_2} {nom_joueur_2} - {resultat_round[1][0]} score: {resultat_round[1][1]}\n" 
    
    if non_joueur != 0:
        affichage_resultat += f"\nLe nombre de participant étant impaire:\nLe joueurs {non_joueur.prenom} {non_joueur.nom} - numero INE: {non_joueur.numero_ine} n'a pas joué ce Round."
    print(affichage_resultat)
    input("\nPressez \"Entrée\" pour continuer.\n")


def recherche_tournoi(liste_tournois):
    if liste_tournois != None and len(liste_tournois) != 0:
        print("Voici les tournois disponible:\n")
        nombre_tournoi = len(liste_tournois)
        i = 1
        for liste in liste_tournois:
            print(f"{i} -> {liste}")
            i += 1

        choix = int(input("\nEntrez le numero du fichier à sélectionner ou 0 pour quitter:\n"))
        
        while True:    
            if choix == 0:
                return None

            elif 1 <= choix <= len(liste):
                choix -= 1
                fichier_tournoi = liste_tournois[choix]
                return fichier_tournoi

            else:
                print(f"Choix invalide, veuillez entrée un nombre compris entre 0 et {nombre_tournoi}")
    
    else:
        print("il n'y a aucun tournoi de disponible pour le moment.")


def affichage_resumer(tournoi, liste_joueurs):
    print(f"\nVoici le resumer tu tournoi:\n")
    print(f"Nombre de tours: {tournoi.nombre_de_tours}\n")
    print(f"Round effectués: {tournoi.tour_actuel}\n")
    print(f"Liste des joueurs inscrit au tournoi {tournoi.nom} de {tournoi.lieu}:")
    liste_triee = sorted(liste_joueurs, key=lambda joueur: joueur.nom)
    for affichage_liste in liste_triee:
        print(affichage_liste)
    print(f"Renarque du directeur du tournoi: {tournoi.remarque}\n")
    if tournoi.tour_actuel >=1:
        print(f"Voici le résumer des Rounds du tournois:\n")
        for round in tournoi.liste_des_tours["round"]:
            print(f"\n{round}")
            for liste_round in tournoi.liste_des_tours["round"][round]:
                print(f"\n{liste_round}")





def choix_resume():
    print("\nAffichage des rapports:\n")
    choix = input("Choisissez une option:\n1. Pour la liste de tous les joueurs\n2. Pour la liste de tous les tournois\n3. Pour quitter:\n") 
    while True:
        if choix == "1":
            return choix
        if choix == "2":
            return choix
        if choix == "3":
            return choix
        else:
            print("Choix invalide, veuillez entrée un nombre compris entre 0 et 3")

def fin_du_tournoi():
    pass


def menu():
    while True:
        
        print("\n\nMenu\nchoisissez une option:\n1. Création d'un nouveau joueur\n2. Création d'un nouveau tournoi\n3. Ajoute un joueur au tournoi:\n4. Lancer / reprendre le tournoi\n5. Afficher le resumer des données\n6. Quitter l'applicaiton du tournoi")
        choix = input("Saisir 1, 2, 3, 4, 5 ou 6:\n")
        
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
            print("Ajoute un joueur au tournoi:\n")
            return choix

        if choix == "4":
            clear_terminal()
            print("Lancement / reprise d'un tournoi:\n")
            return choix

        if choix == "5":
            clear_terminal()
            print("Résumer des données:\n")
            return choix

        if choix == "6":
            clear_terminal()
            return choix

        else:
            print("Choix invalide, Réessayer.")
