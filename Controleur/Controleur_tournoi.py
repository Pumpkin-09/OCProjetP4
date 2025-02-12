import json
import os
import datetime
from Models.Models_donnees import Tournoi, Joueur
from Models.Models_round import Tour, Match
from Vue.Vue_tournoi import AffichageTournoi
from Vue.Vue_round import AffichageRound
from Vue.Vue_menu import AffichageMenu
from Controleur.Controleur_joueur import ControleJoueur


class ControleTournoi:

    def __init__(self, donnees_joueurs):
        self.setting_joueurs = donnees_joueurs

    @staticmethod
    def creation_tournoi():
        dossier = "tournoi"
        os.makedirs(dossier, exist_ok=True)
        info_tournoi = AffichageTournoi.nouveau_tournoi()
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

    def recuperation_donnees_tournoi(self, choix_tournoi):
        dossier_tournoi = "tournoi"
        if choix_tournoi is None:
            return None
        
        chemin_tournoi = os.path.join(dossier_tournoi, choix_tournoi)
        if not os.path.exists(chemin_tournoi):
            affichage_mot = "\nLe tournoi n'a pas été trouvé.\nVeuillez vérifier vos données ou créer un nouveau tournoi."
            AffichageRound.affichage_simple(affichage_mot)
            return None

        else:
            with open(chemin_tournoi, "r") as f:
                settings = json.load(f)

            liste_des_joueurs = []

            if len(settings["liste des joueurs"]) != 0:
                for joueurs in settings["liste des joueurs"]:
                    donnees_joueur = self.setting_joueurs[joueurs[0]]
                    joueur = Joueur(donnees_joueur["numero ine"], donnees_joueur["nom"],
                                    donnees_joueur["prenom"], donnees_joueur["date de naissance"], joueurs[1])
                    liste_des_joueurs.append(joueur)

            tournoi = Tournoi(settings["nom"], settings["lieu"], settings["date de debut"], settings["date de fin"],
                            settings["remarque"], settings["nombre de tours"], settings["tour actuel"],
                            liste_des_joueurs, settings["liste des tours"])
            return tournoi

class DonneesTournoi:

    @classmethod
    def recuperation_date_heure(cls):
        date_heure_actuel = datetime.datetime.now()
        format_date_heure = date_heure_actuel.strftime("%d/%m/%Y %H:%M")
        return format_date_heure

    @classmethod
    def liste_des_tournois(cls):
        # affiche une liste de fichier .json comprenant le mot "tournoi" dans leur titre
        dossier = "tournoi"
        fichier_json = []
        if not os.path.exists(dossier):
            affichage_mot = "\nAucun tournoi n'a été trouvé, veuillez en créer un."
            AffichageRound.affichage_simple(affichage_mot)
            return None
        for fichier in os.listdir(dossier):
            if fichier.endswith(".json") and "tournoi" in fichier.lower():
                fichier_json.append(fichier)
        if set(fichier_json) == 0:
            return None
        return fichier_json


class ExecutionTournoi:
    def __init__(self, controle_tournoi):
        self.tournoi = controle_tournoi

    def demarer_tournoi(self):
        non_joueur = None
        resultat = []
        self.tour_actuel += 1
        liste_des_joueurs = self.liste_des_joueurs
        tour_en_cours = Tour(liste_des_joueurs)
        tour_en_cours.randomiseur_tour1()
        liste_de_match = tour_en_cours.association_joueurs(self)
        date_heure_debut = DonneesTournoi.recuperation_date_heure()
        non_joueur = tour_en_cours.non_joueur
        AffichageRound.affichage_round(self, liste_de_match, date_heure_debut, non_joueur)
        for joueurs_match in liste_de_match:
            matchs = Match(joueurs_match)
            gagant = AffichageTournoi.choix_gagants(joueurs_match)
            resultat_match = matchs.attribution_point(gagant)
            resultat.append(resultat_match)
        date_heure_fin = DonneesTournoi.recuperation_date_heure()
        numero_round = f"Round {self.tour_actuel} \ndebut:{date_heure_debut}\nfin:{date_heure_fin}\n"
        self.liste_des_tours["round"][numero_round] = resultat
        AffichageRound.affichage_resultat_match(self, resultat, date_heure_fin, non_joueur)
        self.sauvegard()
        choix = AffichageMenu.quitter()
        if choix:
            raise SystemExit
        else:
            pass

    def continuer_tournoi(self):
        while self.tour_actuel < self.nombre_de_tours:
            non_joueur = None
            resultat = []
            liste_des_joueurs = self.liste_des_joueurs
            tour_en_cours = Tour(liste_des_joueurs)
            tour_en_cours.triage_par_points()
            liste_de_match = tour_en_cours.association_joueurs(self)
            if liste_de_match is None or len(liste_de_match) == 0:
                AffichageTournoi.fin_tournoi()
                AffichageRound.affichage_resumer(self)
                return
            self.tour_actuel += 1
            date_heure_debut = DonneesTournoi.recuperation_date_heure()
            non_joueur = tour_en_cours.non_joueur
            AffichageRound.affichage_round(self, liste_de_match, date_heure_debut, non_joueur)
            for joueurs_match in liste_de_match:
                matchs = Match(joueurs_match)
                gagant = AffichageTournoi.choix_gagants(joueurs_match)
                resultat_match = matchs.attribution_point(gagant)
                resultat.append(resultat_match)
            date_heure_fin = DonneesTournoi.recuperation_date_heure()
            numero_round = f"Round {self.tour_actuel} \ndebut:{date_heure_debut}\nfin:{date_heure_fin}\n"
            self.liste_des_tours["round"][numero_round] = resultat
            AffichageRound.affichage_resultat_match(self, resultat, date_heure_fin, non_joueur)
            self.sauvegard()
            choix = AffichageMenu.quitter()
            if choix:
                raise SystemExit
        AffichageTournoi.tour_tournoi_max()
        AffichageRound.affichage_resumer(self)
