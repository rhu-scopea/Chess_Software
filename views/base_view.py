#! /usr/bin/env python3
# coding: utf-8
import argparse
import datetime
import re


class View:

    def ask_input(self, message, input_constraint="", required=False):
        """
        Fonction to ask an input and control it with regex
        :param message: Message to show to the user
        :param input_constraint: Regex or Type of input (Ex: Integer, Float ou Date)
        :param required: True or False
        :return: the input if match with the constraints
        """
        input_response = None

        while not input_response:
            input_response = input("\n" + message + "\nPour quiter la saise, tappez 'Q'\n")
            if required and not input_response:
                print("C'est un champ requis, merci de saisir une valeur\n")
            elif input_response:
                input_test = self.check_input(input_response, input_constraint)
                if input_test['error']:
                    input_response = None
                else:
                    input_response = input_test['input_response']
            else:
                return input_response

        return input_response

    def check_input(self, input_response, input_constraint):

        error = False

        if re.match("q|Q", input_response):
            print("Saisie annulée\n")
            return exit()

        if input_constraint:
            if input_constraint.lower() == "float":
                try:
                    input_response = float(input_response)
                except ValueError:
                    print("Merci de saisir un nombre décimal correct\n")
                    error = True

            elif input_constraint.lower() == "integer":
                try:
                    input_response = int(input_response)
                except ValueError:
                    print("Merci de saisir un nombre entier correct\n")
                    error = True

            elif input_constraint.lower() == "date":
                try:
                    input_response = datetime.datetime.strptime(input_response, "%d/%m/%y").date()
                except ValueError:
                    print("Veuillez saisir une date au format jj/mm/aa")
                    error = True
            else:
                input_test = re.match(input_constraint, input_response)
                if not input_test:
                    print("Votre saisie est incorrecte")
                    error = True
                    input_response = None
        return {'input_response': input_response, 'error': error}

    def get_list_to_print(self, list, message=""):
        message = message + "\n" or message
        num = 0
        for item in list:
            num += 1
            message += f"[{num}] : {item}\n"
        return message

    def prompt_menu(self):
        print("""
        Bienvenu sur Chess Master Tournament
        
        Veuillez choisir la section désirée :
        1. Créer un tournoi
        2. Editer un tournoi
        3. Afficher les tournois
        4. Créer des joueurs
        5. Afficher les joueurs
        *************************************
        """)
        return self.ask_input("Veuillez saisir le numéro correspondant à votre choix", '[1-5]', True)

    def show_tournament(self, tournament):
        str = f"""
                        Le tournoi {tournament.name}, prendra place à {tournament.place} """
        if tournament.duration == 1:
            str += f"""la journée du {tournament.start_date} """
        else:
            str += f"""du {tournament.start_date} au {tournament.end_date}"""
        str += f"""
                        Ce tournoi se déroulera en {tournament.turns} tours avec un contrôle du temps de type {tournament.time_control}"""
        if tournament.description:
            str += f"""
                        *****************************************************        
                        Description du Tournoi :
                        {tournament.description}
                        """
        if tournament.players:
            str += f"""
                        *****************************************************
                        Joueurs :
                    """
            for player in tournament.players:
                str += f"\n{player}"
        print(str)

    def show_all_tournaments(self, tournaments):
        print("Name\t\tPlace\t\tStart date\t\tEnd date\t\tTurns\t\tNumber of players\t\tTime control")

        for tournament in tournaments:
            print(
                tournament["name"] + "\t\t" +
                tournament["place"] + "\t\t" +
                tournament["start_date"] + "\t\t" +
                tournament["end_date"] + "\t\t" +
                str(tournament["turns"]) + "\t\t" +
                str(len(tournament["players"])) + "\t\t" +
                str(tournament["time_control"])
            )
