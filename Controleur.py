import json
import Models



def main():

    fichier_joueurs = "joueurs.json"
    with open(fichier_joueurs, "r") as f:
        donnees_joueurs = json.load(f)

        liste_joueurs = []
        for cle, valeurs in donnees_joueurs.items():
            nom = valeurs.get("nom")
            prenom = valeurs.get("prenom")
            date_de_naissance = valeurs.get("date de naissance")
            numero_ine = valeurs.get("numero ine")
            nombre_de_points = valeurs.get("nombre_de_points")

            joueur = Models.Joueur(nom, prenom, date_de_naissance, numero_ine, nombre_de_points, [])
            liste_joueurs.append(joueur)

    premier_tournoi = Models.Tournoi("tournoi test", "Metz", "01/12/2024", "06/12/2024", 1, "rien", liste_joueurs, "rien")

    tour_en_cours = Models.Tour(liste_joueurs, 1)
    tour_en_cours.randomiseur_tour1()
    liste_pour_match = []
    liste_pour_match = tour_en_cours.association_joueurs()
    resultat = []
    for joueurs_match in liste_pour_match:
        matchs = Models.Match(joueurs_match)
        # definir ici les gagants des matchs via Vue
        resultat.append(matchs.attribution_point())
        # faire un affichage (temporaire) de la liste des gagnants
    affichage_resultat = f"Le Round {tour_en_cours.numero_round} en fini.\nvoici la liste des scors:\n"
    tour_en_cours.triage_par_points()
    for round_scors in tour_en_cours.liste_de_joueurs:
        affichage_resultat+= f"{round_scors.prenom} {round_scors.nom_de_famille} - score: {round_scors.nombre_de_points}\n"
    print(affichage_resultat)

    while premier_tournoi.tour_actuel < premier_tournoi.nombre_de_tours:
        premier_tournoi.tour_actuel += 1
        tour_en_cours.numero_round += 1
        tour_en_cours.triage_par_points()
        liste_pour_match = tour_en_cours.association_joueurs()
        for joueurs_match in liste_pour_match:
            matchs = Models.Match(joueurs_match)
            # definir ici les gagants via Vue
            resultat.append(matchs.attribution_point())
        affichage_resultat = f"Le Round {tour_en_cours.numero_round} en fini.\nvoici la liste des scors:\n"
        tour_en_cours.triage_par_points()
        for round_scors in tour_en_cours.liste_de_joueurs:
            affichage_resultat+= f"{round_scors.prenom} {round_scors.nom_de_famille} - score: {round_scors.nombre_de_points}\n"
        print(affichage_resultat)
    


    resume = f"Le tournoi est fini avec un total de {premier_tournoi.tour_actuel} tours.\nvoici la liste des scors:\n"
    tour_en_cours.triage_par_points()
    for liste_des_scors in tour_en_cours.liste_de_joueurs:
        resume += f"{liste_des_scors.prenom} {liste_des_scors.nom_de_famille} - score: {liste_des_scors.nombre_de_points}\n"

    return resume






print(main())


