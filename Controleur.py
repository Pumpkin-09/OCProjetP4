import json
import os
from Models import Joueur, Tour, Tournoi, Match
from Vue import menu, nouveau_joueur, nouveau_tournoi, tournoi_en_cours, choix_gagants, affichage_resultat_match, affichage_round



def enregistrement_joueur(infos_joueur):
        fichier = "joueurs.json"
        if not os.path.exists(fichier):
            with open(fichier, "w")as f:
                json.dump({},f)
        
        with open(fichier, "r") as f:
            settings = json.load(f)

        joueur = { infos_joueur[3]: 
            {
            "nom": infos_joueur[0],
            "prenom": infos_joueur[1],
            "date de naissance": infos_joueur[2],
            "numero ine": infos_joueur[3],
            "nombre_de_points": 0.0        
            }
        }   
        settings.update(joueur)
        with open(fichier, "w") as f:
            json.dump(settings, f, indent=4)


def ajout_liste_match(tournoi, liste_pour_match):
    liste_match = []

    for match in liste_pour_match:
        match_list = (match[0].numero_ine, match[1].numero_ine)
        liste_match.append(match_list)

    tournoi.liste_des_tours.append(liste_match)


def enregistrement_tournoi(tournoi):
    fichier_tournoi = f"tournoi_{tournoi.nom}_{tournoi.lieu}.json"

    if not os.path.exists(fichier_tournoi):
        with open(fichier_tournoi, "w")as f:
            json.dump({},f)
    
    with open(fichier_tournoi, "r") as f:
        settings = json.load(f)

    donnees_tournoi = {tournoi.nom: 
        {
        "nom": tournoi.nom,
        "lieu": tournoi.lieu,
        "date de debut": tournoi.date_de_debut,
        "date de fin": tournoi.date_de_fin,
        "remarque": tournoi.remarque,
        "nombre de tours": tournoi.nombre_de_tours,
        "liste des joueurs" : tournoi.liste_des_joueurs,
        "tour actuel" : tournoi.tour_actuel,
        "liste_des_tours" : tournoi.liste_des_tours
        }
    }   
    settings.update(donnees_tournoi)
    with open(fichier_tournoi, "w") as f:
        json.dump(settings, f, indent=4)


def demarer_tournoi(tournoi, liste_joueurs):
    resultat = []
    liste_pour_match = []

    for ajout_joueur in liste_joueurs:
        tournoi.liste_des_joueurs.append(ajout_joueur.numero_ine)
    tournoi.tour_actuel = 1
    enregistrement_tournoi(tournoi)
    tour_en_cours = Tour(liste_joueurs, 1)
    tour_en_cours.randomiseur_tour1()
    liste_pour_match = tour_en_cours.association_joueurs()
    ajout_liste_match(tournoi, liste_pour_match)
    affichage_round(tour_en_cours, liste_pour_match)

    for joueurs_match in liste_pour_match:
        matchs = Match(joueurs_match)
        gagant = choix_gagants(matchs)
        resultat.append(matchs.attribution_point(gagant))
    tour_en_cours.enregistrement_resultat
    affichage_resultat_match(tour_en_cours)
  

def reprise_du_tournoi(tournoi, tour_en_cours):
    while tournoi.tour_actuel < tournoi.nombre_de_tours:
        tournoi.tour_actuel += 1
        tour_en_cours.numero_round += 1
        tour_en_cours.triage_par_points()
        liste_pour_match = tour_en_cours.association_joueurs()
        resultat = []
        for joueurs_match in liste_pour_match:
            matchs = Match(joueurs_match)
            gagant = choix_gagants(matchs)
            resultat.append(matchs.attribution_point(gagant))
        affichage_resultat_match(tour_en_cours)


def recuperation_donnees_json(liste_joueurs):
    fichier_joueurs = "joueurs.json"
    with open(fichier_joueurs, "r") as f:
        donnees_joueurs = json.load(f)

        for cle, valeurs in donnees_joueurs.items():
            nom = valeurs.get("nom")
            prenom = valeurs.get("prenom")
            date_de_naissance = valeurs.get("date de naissance")
            numero_ine = valeurs.get("numero ine")
            nombre_de_points = valeurs.get("nombre_de_points")

            joueur = Joueur(nom, prenom, date_de_naissance, numero_ine, nombre_de_points, [])
            liste_joueurs.append(joueur)

       





def main():
    liste_joueurs = []

    while True:
        choix_menu = menu() 
        if choix_menu == "1":
            #ajout d'un joueur à la liste des joueurs
            information_joueur = nouveau_joueur()
            joueur = Joueur(information_joueur[0], information_joueur[1], information_joueur[2], information_joueur[3])
            liste_joueurs.append(joueur)
            enregistrement_joueur(information_joueur)

        if choix_menu == "2":
            # création d'un nouveau torunoi
            creation_tournoi = nouveau_tournoi()
            tournoi = Tournoi(creation_tournoi[0], creation_tournoi[1], creation_tournoi[2], creation_tournoi[3], creation_tournoi[4], creation_tournoi[5])
            enregistrement_tournoi(tournoi)

        if choix_menu == "3":
            # lancement du tournoi
            if tournoi.tour_actuel == 0 and tournoi.nom != None :
                # si le tournoi est tour zero (il n'a pas encore commencer) lancement du tournoi
                demarer_tournoi(tournoi, liste_joueurs)
            
            if tournoi.tour_actuel != 0 :
                # reprise du tournoi avec un recapitulatif des informations
                recuperation_donnees_json(liste_joueurs)
                reprise_du_tournoi()

        if choix_menu == "5":
            # fin de l'application
            return print("Au revoir")
        








main()


