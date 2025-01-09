import json
import os
import shutil
from Models import Tour, Tournoi, Match, Joueur
from Vue import quitter, menu, nouveau_joueur, nouveau_tournoi, tournoi_en_cours, fin_du_tournoi, recherche_joueur, choix_gagants, affichage_resultat_match, affichage_round



def gestion_joueurs(tournoi):
    liste_joueurs = []
    for id_joueurs in tournoi.liste_des_joueurs:
        joueur = Joueur(id_joueurs[0], id_joueurs[1])
        liste_joueurs.append(joueur)
    return liste_joueurs


def base_donnees_joueurs():
    fichier_joueurs = "joueurs.json"
    with open(fichier_joueurs, "r") as f:
        donnees_joueurs = json.load(f)
    return donnees_joueurs


def enregistrement_joueur(infos_joueur):
    fichier = "joueurs.json"
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


def mis_a_jour_score(liste_des_joueurs, resultat):
    for liste in liste_des_joueurs:
        for score in resultat:
            if score[0][0] in liste.numero_ine:
                liste.nombre_de_points += score[0][1]
            if score[1][0] in liste.numero_ine:
                liste.nombre_de_points += score[1][1]
            if score[0][0] and score [1][0] not in liste. numero_ine:
                non_joueur = liste
                return non_joueur


def creation_fichier_tournoi(tournoi):
    dossier = "tournoi"
    os.makedirs(dossier, exist_ok=True)

    date_nom = tournoi.date_de_debut.replace("/", "")
    fichier_tournoi = f"tournoi_{tournoi.nom}_{tournoi.lieu}_{date_nom}.json"

    chemin_fichier = os.path.join(dossier, fichier_tournoi)

    if not os.path.exists(chemin_fichier):
        with open(chemin_fichier, "w")as f:
            json.dump({},f)
    
    with open(chemin_fichier, "r") as f:
        settings = json.load(f)

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


def sauvegard_tournoi(tournoi):
    dossier = "tournoi"
    date_nom = tournoi.date_de_debut.replace("/", "")
    fichier_tournoi = f"tournoi_{tournoi.nom}_{tournoi.lieu}_{date_nom}.json"

    chemin_fichier = os.path.join(dossier, fichier_tournoi)

    if not os.path.exists(chemin_fichier):
        with open(chemin_fichier, "w")as f:
            json.dump({},f)
    
    with open(chemin_fichier, "r") as f:
        settings = json.load(f)

    settings["liste des joueurs"] = tournoi.liste_des_joueurs,
    settings["tour actuel"] = tournoi.tour_actuel,
    settings["liste des tours"] = tournoi.liste_des_tours

    with open(chemin_fichier, "w") as f:
        json.dump(settings, f, indent=4)


def demarer_tournoi(tournoi):
    #A MODIFIER!! rajouter l'heure de debut et de fin des rounds!
    non_joueur = 0
    infos_joueurs = base_donnees_joueurs()
    liste_des_joueurs = gestion_joueurs(tournoi)
    resultat = []
    tournoi.tour_actuel[0] += 1
    tour_en_cours = Tour(liste_des_joueurs)
    tour_en_cours.randomiseur_tour1()
    liste_de_match = tour_en_cours.association_joueurs(tournoi)
    affichage_round(tournoi, liste_de_match, infos_joueurs)
    for joueurs_match in liste_de_match:
        matchs = Match(joueurs_match)
        gagant = choix_gagants(joueurs_match, infos_joueurs)
        resultat_match = matchs.attribution_point(gagant)
        resultat.append(resultat_match)
    non_joueur = mis_a_jour_score(liste_des_joueurs, resultat)
    numero_round = f"round {tournoi.tour_actuel[0]}"
    tournoi.liste_des_tours["round"][numero_round] = resultat
    tournoi.liste_des_joueurs = liste_des_joueurs
    affichage_resultat_match(tournoi, resultat, infos_joueurs, non_joueur)
    sauvegard_tournoi(tournoi)
    choix = quitter()
    if choix:
        raise SystemExit
    else:
        continuer_tournoi(tournoi)


def continuer_tournoi(tournoi): # PAS FINI! rajouter la date et l'heure!
    while tournoi.tour_actuel[0] < tournoi.nombre_de_tours:
        non_joueur = 0
        infos_joueurs = base_donnees_joueurs()
        liste_des_joueurs = gestion_joueurs(tournoi)
        resultat = []
        tournoi.tour_actuel[0] += 1
        tour_en_cours = Tour(liste_des_joueurs)
        tour_en_cours.triage_par_points()
        liste_de_match = tour_en_cours.association_joueurs(tournoi)
        affichage_round(tournoi, liste_de_match, infos_joueurs)
        for joueurs_match in liste_de_match:
            matchs = Match(joueurs_match)
            gagant = choix_gagants(joueurs_match, infos_joueurs)
            resultat_match = matchs.attribution_point(gagant)
            resultat.append(resultat_match)
        non_joueur = mis_a_jour_score(liste_des_joueurs, resultat)
        numero_round = f"round {tournoi.tour_actuel[0]}"
        tournoi.liste_des_tours["round"][numero_round] = resultat
        tournoi.liste_des_joueurs = liste_des_joueurs
        affichage_resultat_match(tournoi, resultat, infos_joueurs, non_joueur)
        sauvegard_tournoi(tournoi)
        choix = quitter()
        if choix:
            raise SystemExit
    fin_du_tournoi()


def recuperation_donnees_tournoi():
    dossier = "tournoi"
    lancement_tournoi = tournoi_en_cours()
    fichier_tournoi = f"tournoi_{lancement_tournoi[0]}_{lancement_tournoi[1]}_{lancement_tournoi[2]}.json"
    chemin_complet = os.path.join(dossier, fichier_tournoi)

    if not os.path.exists(chemin_complet):
        print("\nle tournoi n'as pas été trouvé.\nVeuillez verifier vos informations ou crée un nouveau tournoi.")
    
    else:
        with open(chemin_complet, "r") as f:
            settings = json.load(f)
        tournoi = Tournoi(settings["nom"], settings["lieu"], settings["date de debut"], settings["date de fin"],
                          settings["remarque"], settings["nombre de tours"], settings["tour actuel"],
                          settings["liste des joueurs"], settings["liste des tours"])
        return tournoi








def main():
    joueurs = base_donnees_joueurs()
    while True:
        choix_menu = menu() 
        if choix_menu == "1":
            #ajout d'un joueur à la base de donnees des joueurs
            recherche = recherche_joueur(joueurs)
            if recherche:
                pass

            else:
                information_joueur = nouveau_joueur()
                enregistrement_joueur(information_joueur)

        if choix_menu == "2":
            # création d'un nouveau tournoi
            creation_tournoi = nouveau_tournoi()
            tournoi = Tournoi(creation_tournoi[0], creation_tournoi[1], creation_tournoi[2], creation_tournoi[3], creation_tournoi[4], creation_tournoi[5])
            creation_fichier_tournoi(tournoi)

        if choix_menu == "3":
            # rajouter le cas ou on veux rajouter un joueur juste apres avoir demarer l'appli et que le tournoi est deja crée
            try:
                donnee_joueur = recherche_joueur(joueurs)
                if donnee_joueur not in tournoi.liste_des_joueurs:
                    donnees_joueur = (donnee_joueur, 0.0)
                    tournoi.liste_des_joueurs.append(donnees_joueur)
                    sauvegard_tournoi(tournoi)
                elif donnee_joueur in tournoi.liste_des_joueurs:
                    print(f"Le joueur est deja inscrit au tournoi.")
            except:
                tournoi = recuperation_donnees_tournoi()
                donnee_joueur = recherche_joueur(joueurs)
                if donnee_joueur not in tournoi.liste_des_joueurs:
                    donnees_joueur = (donnee_joueur, 0.0)
                    tournoi.liste_des_joueurs.append(donnees_joueur)
                    sauvegard_tournoi(tournoi)
                elif donnee_joueur in tournoi.liste_des_joueurs:
                    print("Le joueur est deja inscrit au tournoi.")              

        if choix_menu == "4":
            # lancement du tournoi

            tournoi = recuperation_donnees_tournoi()
            if len(tournoi.liste_des_joueurs) == 0:
                recherche_joueur(joueurs)
            
            if tournoi.tour_actuel[0] == 0:
                print("demarage")
                demarer_tournoi(tournoi)
            
            else:
                continuer_tournoi(tournoi)
                print("continu")


        if choix_menu == "5":
            # fin de l'application
            return print("Au revoir")
        







if __name__ == "__main__":
    main()


