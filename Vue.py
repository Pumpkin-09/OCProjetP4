import datetime


def clear_terminal(row, col):
    print("\033[2J", end="")
    print(f"\033[{row};{col}H", end="")


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


def choix_gagants(matchs):
    clear_terminal(6,6)
    while True:
        texte = (f"Séléctionnez le gagnant du match:\nPour {matchs.joueur_1.nom_de_famille} {matchs.joueur_1.prenom} numero INE: {matchs.joueur_1.numero_ine} gagant, entrée 1\nPour {matchs.joueur_2.nom_de_famille} {matchs.joueur_2.prenom} numero INE: {matchs.joueur_2.numero_ine} gagant, entrée 2\nPour un match nul, entrée 3:\n")
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
    clear_terminal(6,6)
    nom_tournoi = verification_input("Veuillez saisir le nom du tournois:\n", lambda nom_tournoi: nom_tournoi != "")
    lieu_tournoi = verification_input("Veuillez saisir le lieu du tournois:\n", lambda lieu_tournoi: lieu_tournoi != "")
    date_debut_tournoi = verification_input("Veuillez saisir la date de début du tournoi:\n(date au format JJ/MM/AAAA)\n", verification_date)
    date_fin_tournoi = verification_input("Veuillez saisir la date de fin du tournoi:\n(date au format JJ/MM/AAAA)\n", verification_date)
    choix_remarque = input("Voulez vous ajouter une remarque pour ce tournoi?\nOui\nNon\n")
    if choix_remarque == "oui":
        remarque = input("Indiquer les remarques concernant ce tournoi:\n")
    else:
        remarque = " "

    choix_nombre_tour = input ("Le nombre de tour pour le tournoi est par defaut de 4.\nVoulez vous changer le nombre de tour?\nOui\nNon\n")
    if choix_nombre_tour == "oui":
        nombre_de_tour_str = input("Veuillez saisir le nombre de tour pour ce tournoi:\n")
        nombre_de_tour = int(nombre_de_tour_str)
    else:
        nombre_de_tour = 4
    infos_tournoi = (nom_tournoi, lieu_tournoi, date_debut_tournoi, date_fin_tournoi, remarque, nombre_de_tour)
    return infos_tournoi


def nouveau_joueur():
    clear_terminal(6,6)
    nom = verification_input("Veuillez saisir le Nom du joueur:\n", lambda nom: nom != "")
    prenom = verification_input("Veuillez saisir le Prénom du joueur:\n", lambda prenom: prenom != "")
    date_de_naissance = verification_input("Veuillez saisir la Date de Naissance du joueur:\n(date au format JJ/MM/AAAA)\n", verification_date)
    numero_ine = verification_input("Veuillez saisir le Numero INE du joueur:\n", lambda numero_ine: len(numero_ine) == 7)

    infos_joueur = (nom, prenom, date_de_naissance, numero_ine)
    return infos_joueur


def affichage_round(tour_en_cours, liste_pour_match):
    clear_terminal(6,6)
    affichage_round = f"Voici la liste des matchs pour le Round {tour_en_cours.numero_round}:\n"
    for match in liste_pour_match:
        affichage_round += f"{match[0].prenom} {match[0].nom_de_famille} - {match[0].numero_ine} contre {match[1].prenom} {match[1].nom_de_famille} - {match[1].numero_ine}\n" 
    print(affichage_round)
    input("Pressez \"Entrée\" pour continuer\n")



def affichage_resultat_match(tour_en_cours):
    clear_terminal(6,6)
    affichage_resultat = f"Le Round {tour_en_cours.numero_round} en fini.\nvoici la liste des scors:\n"
    tour_en_cours.triage_par_points()
    for round_scors in tour_en_cours.liste_de_joueurs:
        affichage_resultat+= f"{round_scors.prenom} {round_scors.nom_de_famille} - score: {round_scors.nombre_de_points}\n"
    print(affichage_resultat)


def tournoi_en_cours():
    clear_terminal(6,6)
    pass


def menu():
    clear_terminal(6,6)
    while True:
        
        print("Menu\nchoisissez une option:\n1. Ajouter un nouveau joueur\n2. Création d'un nouveau tournoi\n3. Lancer / reprendre le tournoi\n4. Résumé du tournoi en cours\n5. Quitter l'applicaiton du tournoi")
        choix = input("Saisir 1, 2, 3, 4 ou 5:\n")
        
        if choix == "1":
            print("Ajout d'un nouveau joueur:\n")
            return choix
        
        if choix == "2":
            print("Création d'un nouveau tournoi:\n")
            return choix
        
        if choix == "3":
            print("Lancement / reprise du tournoi:\n")
            return choix

        if choix == "4":
            print("Résumer du tournoi:\n")
            return choix

        if choix == "5":
            return choix

        else:
            print("Choix invalide, Réessayer.")

        
