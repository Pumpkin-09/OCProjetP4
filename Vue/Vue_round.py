from Vue.Vue_verification import AffichageVerification


class AffichageRound:

    @staticmethod
    def affichage_simple(affichage_mot):
        print(affichage_mot)

    @staticmethod
    def affichage_round(tournoi, liste_de_match, date_heure_debut, non_joueur):
        AffichageVerification.clear_terminal()
        affichage_round = f"Voici la liste des matchs pour le Round {tournoi.tour_actuel} {date_heure_debut}:\n"
        for match in liste_de_match:
            prenom1 = match[0].prenom
            nom1 = match[0].nom
            ine1 = match[0].numero_ine
            prenom2 = match[1].prenom
            nom2 = match[1].nom
            ine2 = match[1].numero_ine

            affichage_round += f"\n{prenom1} {nom1} INE {ine1} - contre - {prenom2} {nom2} INE {ine2}\n"

        if non_joueur != 0:
            prenom = non_joueur.prenom
            nom = non_joueur.nom
            ine = non_joueur.numero_ine
            affichage_round += "\nLe nombre de participants étant impaire:\n"
            affichage_round += f"Le joueur {prenom} {nom} - numero INE: {ine} ne jouera pas ce Round."

        print(affichage_round)
        input("\nPressez \"Entrée\" pour terminer le Round et définir les gagnants.\n")

    @staticmethod
    def affichage_resultat_match(tournoi, resultat, date_heure_fin, non_joueur):
        AffichageVerification.clear_terminal()
        affichage = f"Le Round {tournoi.tour_actuel} est fini.\nVoici les résultats des matchs {date_heure_fin}:\n"
        for resultat_round in resultat:
            for liste in tournoi.liste_des_joueurs:
                if resultat_round[0][0] in liste.numero_ine:
                    prenom1 = liste.prenom
                    nom1 = liste.nom
                    ine1 = resultat_round[0][0]
                    scor1 = resultat_round[0][1]
                if resultat_round[1][0] in liste.numero_ine:
                    prenom2 = liste.prenom
                    nom2 = liste.nom
                    ine2 = resultat_round[1][0]
                    scor2 = resultat_round[1][1]

            affichage += f"\n{prenom1} {nom1} {ine1} score: {scor1} contre {prenom2} {nom2} {ine2} score: {scor2}\n"

        if non_joueur != 0:
            prenom = non_joueur.prenom
            nom = non_joueur.nom
            ine = non_joueur.numero_ine
            affichage += "\nLe nombre de participants étant impaire:\n"
            affichage += f"Le joueur {prenom} {nom} - numero INE: {ine} n'a pas joué ce Round."
        print(affichage)
        input("\nPressez \"Entrée\" pour continuer.\n")

    @staticmethod
    def affichage_resumer(tournoi):
        print("-----------------------------------------------------------------------")
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
            print("\nVoici le résumé des Rounds du tournoi:")
            for round in tournoi.liste_des_tours["round"]:
                print(f"\n--------\n{round}")
                for match in tournoi.liste_des_tours["round"][round]:
                    for liste in tournoi.liste_des_joueurs:
                        if match[0][0] in liste.numero_ine:
                            prenom1 = liste.prenom
                            nom1 = liste.nom
                            ine1 = match[0][0]
                            scor1 = match[0][1]
                        if match[1][0] in liste.numero_ine:
                            prenom2 = liste.prenom
                            nom2 = liste.nom
                            ine2 = match[1][0]
                            scor2 = match[1][1]

                    print(f"{prenom1} {nom1} - {ine1} score: {scor1} contre {prenom2} {nom2} - {ine2} score: {scor2}")
        input("\nPressez \"Entrée\" pour quitter le résumé")
        print("-----------------------------------------------------------------------")
