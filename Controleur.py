import json
import os
import datetime
from Models import Tour, Tournoi, Match, Joueur
from Vue import quitter, menu, nouveau_joueur, nouveau_tournoi, recherche_tournoi, fin_du_tournoi, recherche_joueur, choix_gagants, affichage_resultat_match, affichage_round




def enregistrement_joueur():
    fichier = "joueurs.json"
    infos_joueur = nouveau_joueur()
    if not os.path.exists(fichier):
        with open(fichier, "w")as f:
            json.dump({},f)
    
    with open(fichier, "r") as f:
        settings = json.load(f)

    if infos_joueur[3] in settings:
        pass

    else:
        joueur = { infos_joueur[3]: 
            {
            "nom": infos_joueur[0],
            "prenom": infos_joueur[1],
            "date de naissance": infos_joueur[2],
            "numero ine": infos_joueur[3],       
            }
        }   
        settings.update(joueur)
        with open(fichier, "w") as f:
            json.dump(settings, f, indent=4)


def creation_fichier_tournoi():
    dossier = "tournoi"
    os.makedirs(dossier, exist_ok=True)
    info_tournoi = nouveau_tournoi()
    date_nom = info_tournoi[2].replace("/", "")
    fichier_tournoi = f"tournoi_{info_tournoi[0]}_{info_tournoi[1]}_{date_nom}.json"

    chemin_fichier = os.path.join(dossier, fichier_tournoi)

    if not os.path.exists(chemin_fichier):
        with open(chemin_fichier, "w")as f:
            json.dump({},f)
    
    with open(chemin_fichier, "r") as f:
        settings = json.load(f)

    tournoi = Tournoi(info_tournoi[0], info_tournoi[1], info_tournoi[2], info_tournoi[3], info_tournoi[4], info_tournoi[5])

    donnees_tournoi = {
        "nom": tournoi.nom,
        "lieu": tournoi.lieu,
        "date de debut": tournoi.date_de_debut,
        "date de fin": tournoi.date_de_fin,
        "remarque": tournoi.remarque,
        "nombre de tours": tournoi.nombre_de_tours,
        "tour actuel" : tournoi.tour_actuel,
        "liste des joueurs" : tournoi.liste_des_joueurs,
        "liste des tours" : tournoi.liste_des_tours
        }
    settings.update(donnees_tournoi)
    with open(chemin_fichier, "w") as f:
        json.dump(settings, f, indent=4)
    return tournoi


def ajout_joueur_tournoi(tournoi):
    fichier_joueurs = "joueurs.json"
    with open(fichier_joueurs, "r") as f:
        donnees_joueurs = json.load(f)
        nombre_joueur = len(tournoi.liste_des_joueurs)
    numero_ine_joueur = recherche_joueur(donnees_joueurs, nombre_joueur)
    for verification_joueur in tournoi.liste_des_joueurs:
        if numero_ine_joueur == verification_joueur[0]:
            return
    donnees_joueur = donnees_joueurs[numero_ine_joueur]
    joueur = Joueur(donnees_joueur["numero ine"], donnees_joueur["nom"], donnees_joueur["prenom"], donnees_joueur["date de naissance"])
    joueur_liste = (joueur.numero_ine, joueur.score)
    tournoi.liste_des_joueurs.append(joueur_liste)
    return joueur


def mis_a_jour_score(liste_des_joueurs, tournoi):
    liste_joueurs = []
    for joueurs in liste_des_joueurs:
        joueur_score = [joueurs.numero_ine, joueurs.score]
        liste_joueurs.append(joueur_score)
    tournoi.liste_des_joueurs = liste_joueurs


def recuperation_date_heure():
    date_heure_actuel = datetime.datetime.now()
    format_date_heure = date_heure_actuel.strftime("%d/%m/%Y %H:%M")
    return format_date_heure


def sauvegard_tournoi(tournoi):
    # Remplacement des ancienne donnees liste des joueurs, tour actuel et liste des tours dans le fichier json
    dossier = "tournoi"
    date_nom = tournoi.date_de_debut.replace("/", "")
    fichier_tournoi = f"tournoi_{tournoi.nom}_{tournoi.lieu}_{date_nom}.json"
    chemin_fichier = os.path.join(dossier, fichier_tournoi)

    with open(chemin_fichier, "r") as f:
        settings = json.load(f)

    settings["liste des joueurs"] = tournoi.liste_des_joueurs
    settings["tour actuel"] = tournoi.tour_actuel
    settings["liste des tours"] = tournoi.liste_des_tours

    with open(chemin_fichier, "w") as f:
        json.dump(settings, f, indent=4)


def liste_des_tournois():
    # affiche une liste des fichier .json comprenant le mot "tournoi" dans leurs titre
    dossier = "tournoi"
    fichier_json = []
    if not os.path.exists(dossier):
        return None
    for fichier in os.listdir(dossier):
        if fichier.endswith(".json") and "tournoi" in fichier.lower():
            fichier_json.append(fichier)
    if set(fichier_json) == 0:
        return None
    return fichier_json


def recuperation_donnees_tournoi(choix_tournoi):
    dossier = "tournoi"
    chemin_complet = os.path.join(dossier, choix_tournoi)

    if not os.path.exists(chemin_complet):
        print("\nle tournoi n'as pas été trouvé.\nVeuillez verifier vos informations ou crée un nouveau tournoi.")
    
    else:
        with open(chemin_complet, "r") as f:
            settings = json.load(f)
        tournoi = Tournoi(settings["nom"], settings["lieu"], settings["date de debut"], settings["date de fin"],
                          settings["remarque"], settings["nombre de tours"], settings["tour actuel"],
                          settings["liste des joueurs"], settings["liste des tours"])
        return tournoi


def recuperation_donnees_joueur(tournoi):
    liste_joueurs = []
    fichier_joueurs = "joueurs.json"
    with open(fichier_joueurs, "r") as f:
        donnees_joueurs = json.load(f)
    
    for joueurs in tournoi.liste_des_joueurs:
        donnees_joueur = donnees_joueurs[joueurs[0]]
        joueur = Joueur(donnees_joueur["numero ine"], donnees_joueur["nom"], donnees_joueur["prenom"], donnees_joueur["date de naissance"])
        liste_joueurs.append(joueur)
    return liste_joueurs


def demarer_tournoi(tournoi, liste_des_joueurs):
    non_joueur = None
    resultat = []
    tournoi.tour_actuel += 1
    tour_en_cours = Tour(liste_des_joueurs)
    tour_en_cours.randomiseur_tour1()
    liste_de_match = tour_en_cours.association_joueurs(tournoi)
    date_heure_debut = recuperation_date_heure()
    affichage_round(tournoi, liste_de_match, date_heure_debut)
    for joueurs_match in liste_de_match:
        matchs = Match(joueurs_match)
        gagant = choix_gagants(joueurs_match)
        resultat_match = matchs.attribution_point(gagant)
        resultat.append(resultat_match)
    non_joueur = tour_en_cours.non_joueur
    mis_a_jour_score(liste_des_joueurs, tournoi)
    date_heure_fin = recuperation_date_heure()
    numero_round = f"round {tournoi.tour_actuel}, \ndebut:{date_heure_debut}\nfin:{date_heure_fin}\n"
    tournoi.liste_des_tours["round"][numero_round] = resultat
    affichage_resultat_match(tournoi, liste_des_joueurs, resultat, date_heure_fin, non_joueur)
    sauvegard_tournoi(tournoi)
    choix = quitter()
    if choix:
        raise SystemExit
    else:
        pass


def continuer_tournoi(tournoi, liste_des_joueurs):
    while tournoi.tour_actuel < tournoi.nombre_de_tours:
        non_joueur = None
        resultat = []
        tournoi.tour_actuel += 1
        tour_en_cours = Tour(liste_des_joueurs)
        tour_en_cours.triage_par_points()
        liste_de_match = tour_en_cours.association_joueurs(tournoi)
        date_heure_debut = recuperation_date_heure()
        affichage_round(tournoi, liste_de_match, date_heure_debut)
        for joueurs_match in liste_de_match:
            matchs = Match(joueurs_match)
            gagant = choix_gagants(joueurs_match)
            resultat_match = matchs.attribution_point(gagant)
            resultat.append(resultat_match)
        non_joueur = tour_en_cours.non_joueur
        mis_a_jour_score(liste_des_joueurs, tournoi)
        date_heure_fin = recuperation_date_heure()
        numero_round = f"round {tournoi.tour_actuel}, \ndebut:{date_heure_debut}\nfin:{date_heure_fin}\n"
        tournoi.liste_des_tours["round"][numero_round] = resultat
        affichage_resultat_match(tournoi, liste_des_joueurs, resultat, date_heure_fin, non_joueur)
        sauvegard_tournoi(tournoi)
        choix = quitter()
        if choix:
            raise SystemExit
    fin_du_tournoi()



def main():
    tournoi = None
    liste_des_joueurs = []
    while True:
        choix_menu = menu() 
        if choix_menu == "1": # ajout d'un joueur à la base de donnees des joueurs
            enregistrement_joueur()
        if choix_menu == "2": # création d'un nouveau tournoi
            creation_fichier_tournoi()
            if tournoi != None:
                sauvegard_tournoi(tournoi)
        if choix_menu == "3": # Ajoute un joueur au tournoi
            liste_tournois = liste_des_tournois()
            if liste_tournois != None and tournoi == None:
                choix_tournoi = recherche_tournoi(liste_tournois)
                if choix_tournoi == None:
                    continue
                tournoi = recuperation_donnees_tournoi(choix_tournoi)
            joueurs = ajout_joueur_tournoi(tournoi)
            liste_des_joueurs.append(joueurs)
            if tournoi != None:
                sauvegard_tournoi(tournoi)
        if choix_menu == "4": # lancement du tournoi
            liste_tournois = liste_des_tournois()
            if liste_tournois == None:
                creation_fichier_tournoi()
                liste_tournois = liste_des_tournois()
            if tournoi == None:
                choix_tournoi = recherche_tournoi(liste_tournois)
                if choix_tournoi == None:
                    continue
                tournoi = recuperation_donnees_tournoi(choix_tournoi)
            if len(liste_des_joueurs) != len(tournoi.liste_des_joueurs):
                liste_des_joueurs = recuperation_donnees_joueur(tournoi)
            if len(liste_des_joueurs) == 0:
                joueurs = ajout_joueur_tournoi(tournoi)
                liste_des_joueurs.append(joueurs)
                sauvegard_tournoi(tournoi)
                continue
            if tournoi.tour_actuel == 0:
                demarer_tournoi(tournoi, liste_des_joueurs)
            if tournoi.tour_actuel != tournoi.nombre_de_tours:
                continuer_tournoi(tournoi, liste_des_joueurs)
        if choix_menu == "5":
            # fin de l'application
            if tournoi != None:
                sauvegard_tournoi(tournoi)
            return print("Au revoir")
        







if __name__ == "__main__":
    main()


