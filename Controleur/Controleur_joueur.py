import json
import os
from Models.Models_donnees import Joueur
from Vue.Vue_joueur import AffichageJoueur
from Vue.Vue_round import AffichageRound


class ControleJoueur:

    def __init__(self, tournoi):
        self.tournoi = tournoi

    def ajout_joueur_tournoi(self):

        numero_ine = []
        for ine_joueur in self.liste_des_joueurs:
            numero_ine.append(ine_joueur.numero_ine)
        controle_joueur = ControleJoueur.donnees_joueurs()
        if controle_joueur is None:
            return
        numero_ine_joueur = AffichageJoueur.recherche_joueur(self, controle_joueur, numero_ine)
        if numero_ine_joueur is None:
            return None
        for numero_joueur in numero_ine_joueur:
            donnees_joueur = controle_joueur[numero_joueur]
            joueur = Joueur(donnees_joueur["numero ine"], donnees_joueur["nom"],
                            donnees_joueur["prenom"], donnees_joueur["date de naissance"])
            self.liste_des_joueurs.append(joueur)
        self.sauvegard()

    @classmethod
    def creation_joueur(cls):
        dossier = "joueurs"
        fichier = "joueurs.json"
        os.makedirs(dossier, exist_ok=True)
        chemin_fichier = os.path.join(dossier, fichier)

        if not os.path.exists(chemin_fichier):
            with open(chemin_fichier, "w")as f:
                json.dump({}, f)

        with open(chemin_fichier, "r") as f:
            settings = json.load(f)

        infos_joueur = AffichageJoueur.nouveau_joueur(settings)
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

    @classmethod
    def donnees_joueurs(cls):
        dossier_joueur = "joueurs"
        fichier_joueur = "joueurs.json"
        chemin_joueur = os.path.join(dossier_joueur, fichier_joueur)

        if not os.path.exists(chemin_joueur):
            affichage_mot = "\nLa liste des joueurs n'a pas été trouvée."
            AffichageRound.affichage_simple(affichage_mot)
            affichage_mot = "Veuillez vérifier vos données ou créer un nouveau joueur.\n"
            AffichageRound.affichage_simple(affichage_mot)
            return None

        with open(chemin_joueur, "r") as f:
            donnees_joueurs = json.load(f)
        return donnees_joueurs
