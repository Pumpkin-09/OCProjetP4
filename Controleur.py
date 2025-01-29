import json
import os
import datetime
from Models import Tour, Tournoi, Match, Joueur
from Vue import (menu,
                 quitter,
                 tour_tournoi_max,
                 fin_tournoi,
                 choix_resume,
                 choix_gagants,
                 nouveau_joueur,
                 nouveau_tournoi,
                 recherche_joueur,
                 recherche_tournoi,
                 affichage_round,
                 affichage_resumer,
                 affichage_simple,
                 affichage_resultat_match)



def enregistrement_joueur():
    dossier = "joueurs"
    fichier = "joueurs.json"
    os.makedirs(dossier, exist_ok=True)
    chemin_fichier = os.path.join(dossier, fichier)

    if not os.path.exists(chemin_fichier):
        with open(chemin_fichier, "w")as f:
            json.dump({}, f)

    with open(chemin_fichier, "r") as f:
        settings = json.load(f)

    infos_joueur = nouveau_joueur(settings)
    if infos_joueur is None:
        return

    else:
        joueur = {infos_joueur[3]: {
                        "nom": infos_joueur[0],
                        "prenom": infos_joueur[1],
                        "date de naissance": infos_joueur[2],
                        "numero ine": infos_joueur[3]}
                  }
        settings.update(joueur)
        with open(chemin_fichier, "w") as f:
            json.dump(settings, f, indent=4)


def creation_tournoi():
    dossier = "tournoi"
    os.makedirs(dossier, exist_ok=True)
    info_tournoi = nouveau_tournoi()
    date_nom = info_tournoi[2].replace("/", "")
    fichier_tournoi = f"tournoi_{info_tournoi[0]}_{info_tournoi[1]}_{date_nom}.json"

    chemin_fichier = os.path.join(dossier, fichier_tournoi)
    if not os.path.exists(chemin_fichier):
        with open(chemin_fichier, "w")as f:
            json.dump({}, f)

    with open(chemin_fichier, "r") as f:
        settings = json.load(f)

    donnees_tournoi = {
        "nom": info_tournoi[0],
        "lieu": info_tournoi[1],
        "date de debut": info_tournoi[2],
        "date de fin": info_tournoi[3],
        "remarque": info_tournoi[4],
        "nombre de tours": info_tournoi[5],
        "tour actuel": 0,
        "liste des joueurs": [],
        "liste des tours": {"round": {}, "adversaire": []}
        }
    settings.update(donnees_tournoi)
    with open(chemin_fichier, "w") as f:
        json.dump(settings, f, indent=4)


def ajout_joueur_tournoi(tournoi):
    dossier = "joueurs"
    fichier = "joueurs.json"
    chemin_fichier = os.path.join(dossier, fichier)
    with open(chemin_fichier, "r") as f:
        donnees_joueurs = json.load(f)
    numero_ine = []
    for ine_joueur in tournoi.liste_des_joueurs:
        numero_ine.append(ine_joueur.numero_ine)
    numero_ine_joueur = recherche_joueur(tournoi, donnees_joueurs, numero_ine)
    if numero_ine_joueur is None:
        return None
    for numero_joueur in numero_ine_joueur:
        donnees_joueur = donnees_joueurs[numero_joueur]
        joueur = Joueur(donnees_joueur["numero ine"], donnees_joueur["nom"],
                        donnees_joueur["prenom"], donnees_joueur["date de naissance"])
        tournoi.liste_des_joueurs.append(joueur)
    tournoi.sauvegard()


def recuperation_date_heure():
    date_heure_actuel = datetime.datetime.now()
    format_date_heure = date_heure_actuel.strftime("%d/%m/%Y %H:%M")
    return format_date_heure


def liste_des_tournois():
    # affiche une liste de fichier .json comprenant le mot "tournoi" dans leur titre
    dossier = "tournoi"
    fichier_json = []
    if not os.path.exists(dossier):
        mot = "\nAucun tournoi n'a été trouvé, veuillez en créer un."
        affichage_simple(mot)
        return None
    for fichier in os.listdir(dossier):
        if fichier.endswith(".json") and "tournoi" in fichier.lower():
            fichier_json.append(fichier)
    if set(fichier_json) == 0:
        return None
    return fichier_json


def recuperation_donnees_tournoi(choix_tournoi):
    dossier_tournoi = "tournoi"
    chemin_tournoi = os.path.join(dossier_tournoi, choix_tournoi)
    dossier_joueur = "joueurs"
    fichier_joueur = "joueurs.json"
    chemin_joueur = os.path.join(dossier_joueur, fichier_joueur)

    if not os.path.exists(chemin_tournoi):
        affichage_mot = "\nLe tournoi n'a pas été trouvé.\nVeuillez vérifier vos données ou créer un nouveau tournoi."
        affichage_simple(affichage_mot)
        return None
    if not os.path.exists(chemin_joueur):
        affichage_mot = "\nLa liste des joueurs n'a pas été trouvée."
        mot_affichage = "Veuillez vérifier vos données ou créer un nouveau joueur.\n"
        affichage_simple(affichage_mot)
        affichage_simple(mot_affichage)
        return None

    else:
        with open(chemin_tournoi, "r") as f:
            settings = json.load(f)

        liste_des_joueurs = []
        with open(chemin_joueur, "r") as f:
            donnees_joueurs = json.load(f)
        if len(settings["liste des joueurs"]) != 0:
            for joueurs in settings["liste des joueurs"]:
                donnees_joueur = donnees_joueurs[joueurs[0]]
                joueur = Joueur(donnees_joueur["numero ine"], donnees_joueur["nom"],
                                donnees_joueur["prenom"], donnees_joueur["date de naissance"], joueurs[1])
                liste_des_joueurs.append(joueur)

        tournoi = Tournoi(settings["nom"], settings["lieu"], settings["date de debut"], settings["date de fin"],
                          settings["remarque"], settings["nombre de tours"], settings["tour actuel"],
                          liste_des_joueurs, settings["liste des tours"])
        return tournoi


def demarer_tournoi(tournoi):
    non_joueur = None
    resultat = []
    tournoi.tour_actuel += 1
    liste_des_joueurs = tournoi.liste_des_joueurs
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
    date_heure_fin = recuperation_date_heure()
    numero_round = f"round {tournoi.tour_actuel}, \ndebut:{date_heure_debut}\nfin:{date_heure_fin}\n"
    tournoi.liste_des_tours["round"][numero_round] = resultat
    affichage_resultat_match(tournoi, resultat, date_heure_fin, non_joueur)
    tournoi.sauvegard()
    choix = quitter()
    if choix:
        raise SystemExit
    else:
        pass


def continuer_tournoi(tournoi):
    while tournoi.tour_actuel < tournoi.nombre_de_tours:
        non_joueur = None
        resultat = []
        tournoi.tour_actuel += 1
        liste_des_joueurs = tournoi.liste_des_joueurs
        tour_en_cours = Tour(liste_des_joueurs)
        tour_en_cours.triage_par_points()
        liste_de_match = tour_en_cours.association_joueurs(tournoi)
        if liste_de_match is None:
            fin_tournoi()
            affichage_resumer(tournoi)
            return
        date_heure_debut = recuperation_date_heure()
        affichage_round(tournoi, liste_de_match, date_heure_debut)
        for joueurs_match in liste_de_match:
            matchs = Match(joueurs_match)
            gagant = choix_gagants(joueurs_match)
            resultat_match = matchs.attribution_point(gagant)
            resultat.append(resultat_match)
        non_joueur = tour_en_cours.non_joueur
        date_heure_fin = recuperation_date_heure()
        numero_round = f"round {tournoi.tour_actuel}, \ndebut:{date_heure_debut}\nfin:{date_heure_fin}\n"
        tournoi.liste_des_tours["round"][numero_round] = resultat
        affichage_resultat_match(tournoi, resultat, date_heure_fin, non_joueur)
        tournoi.sauvegard()
        choix = quitter()
        if choix:
            raise SystemExit
    tour_tournoi_max()
    affichage_resumer(tournoi)


def resume_donnees():
    while True:
        choix = choix_resume()
        if choix == "1":
            liste_joueurs = []
            dossier = "joueurs"
            fichier = "joueurs.json"
            try:
                chemin_fichier = os.path.join(dossier, fichier)
                with open(chemin_fichier, "r") as f:
                    donnees_joueurs = json.load(f)
                for ine_joueurs, donnees_joueur in donnees_joueurs.items():
                    joueur = Joueur(donnees_joueur["numero ine"], donnees_joueur["nom"],
                                    donnees_joueur["prenom"], donnees_joueur["date de naissance"])

                    liste_joueurs.append(joueur)
                liste_triee = sorted(liste_joueurs, key=lambda joueur: joueur.nom)
                for affichage in liste_triee:
                    affichage_simple(affichage)
            except FileNotFoundError:
                affichage_mot = "\nPas de joueur enregistré."
                affichage_simple(affichage_mot)
                continue

        if choix == "2":
            liste_tournois = liste_des_tournois()
            if liste_tournois is None:
                continue
            choix_tournoi = recherche_tournoi(liste_tournois)
            if choix_tournoi is None:
                continue
            tournoi = recuperation_donnees_tournoi(choix_tournoi)
            affichage_resumer(tournoi)
        else:
            return


def main():
    tournoi = None
    while True:
        choix_menu = menu()
        if choix_menu == "1":  # ajout d'un joueur a la base de donnees des joueurs
            enregistrement_joueur()

        if choix_menu == "2":  # creation d'un nouveau tournoi
            creation_tournoi()

        if choix_menu == "3":  # Ajoute un joueur au tournoi
            tournoi = None
            liste_tournois = liste_des_tournois()
            if liste_tournois is not None:
                choix_tournoi = recherche_tournoi(liste_tournois)
                if choix_tournoi is None:
                    continue
                tournoi = recuperation_donnees_tournoi(choix_tournoi)
                if tournoi is None:
                    continue
                ajout_joueur_tournoi(tournoi)
                tournoi.sauvegard()

        if choix_menu == "4":  # lancement du tournoi
            tournoi = None
            liste_tournois = liste_des_tournois()
            if liste_tournois is not None:
                choix_tournoi = recherche_tournoi(liste_tournois)
                if choix_tournoi is None:
                    continue
                tournoi = recuperation_donnees_tournoi(choix_tournoi)
                if len(tournoi.liste_des_joueurs) <= 1:
                    mot = "Moins de deux joueurs sont inscrits à ce tournoi, Veuillez en selectionner."
                    affichage_simple(mot)
                    non = ajout_joueur_tournoi(tournoi)
                    if non is None:
                        continue
                    tournoi.sauvegard()
                if tournoi.tour_actuel == 0:
                    demarer_tournoi(tournoi)
                if tournoi.tour_actuel != tournoi.nombre_de_tours:
                    affichage_resumer(tournoi)
                    continuer_tournoi(tournoi)
                if tournoi.tour_actuel == tournoi.nombre_de_tours:
                    tour_tournoi_max()
                    affichage_resumer(tournoi)
                    tournoi = None

        if choix_menu == "5":  # affiche le resume du tournoi choisi
            resume_donnees()

        if choix_menu == "0":  # fin de l'application
            if tournoi is not None:
                tournoi.sauvegard()
            affichage_mot = ("Au revoir")
            affichage_simple(affichage_mot)
            return


if __name__ == "__main__":
    main()
