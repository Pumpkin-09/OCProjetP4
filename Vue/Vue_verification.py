import datetime


class AffichageVerification:

    @staticmethod
    def clear_terminal():
        print("\033[2J", end="")
        print(f"\033[{6};{0}H", end="")

    @staticmethod
    def verification_input(question, condition_validite):
        while True:
            reponse = input(question)
            if condition_validite(reponse):
                return reponse
            else:
                print("Saisie invalide. Veuillez réessayer.")

    @staticmethod
    def verification_date(date_str):
        # Vérification si la date est au format JJ/MM/AAAA
        try:
            jour, mois, annee = map(int, date_str.split('/'))
            datetime.date(annee, mois, jour)
            return True

        except ValueError:
            return False
