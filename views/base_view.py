#! /usr/bin/env python3
# coding: utf-8
import argparse
import datetime
import re


class View():

    def ask_input(self, message, input_constraint="None", required=False, constraint_type=""):
        """
        Fonction to ask an input and control it with regex
        :param required: True or False
        :param constraint_type: Type of input (Integer, Float ou Date)
        :param message: Message to show to the user
        :param input_constraint: Regex
        :return: the input if match with the regex
        """
        input_response = None
        check_input = None
        constraint_test = None
        constraint_type = constraint_type.lower()

        while not check_input:
            input_response = input(message + "\n" + "Pour quiter la saise, tappez 'Q'\n")

            if re.match("q|Q", input_response):
                print("Saisie annulée\n")
                return

            if input_constraint:
                constraint_test = re.match(input_constraint, input_response)

            if constraint_test == False:
                print("Veuillez saisir une valeur correcte")
                break
            else:

                if constraint_type == "float" and isinstance(input_response, float):
                    return input_response

                if constraint_type == "integer" and isinstance(input_response, int):
                    return input_response

                if constraint_type == "date":
                    try:
                        input_response = datetime.datetime.strptime(input_response, "%d/%m/%y")
                        return input_response
                    except ValueError as err:
                        if required and input_response:
                            print("Veuillez saisir une date au format jj/mm/aa")
                        elif not required and not input_response:
                            return

            if required and not input_response:
                print("C'est un champ requis, merci de saisir une valeur\n")

            return

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

    def prompt_for_new_tournament(self):
        name = None
        place = None

        while not name:
            name = input("Veuillez tapper le nom du Tournois : ")
            if not name:
                print("Merci de saisir un nom de tournoi")

        while not place:
            place = input("Veuillez tapper l'emplacement du Tournois : ")
            if not place:
                print("Merci de saisir un emplacement de tournoi")

        args = {"name": name, "place": place}

        return args

    def show_tournament(self, tournament):
        str = f"""
                        Le tournoi {tournament.name}, prendra place à {tournament.place} """
        if tournament.duration == 1:
            str += f"""la journée du {tournament.start_date} """
        else:
            str += f"""du {tournament.start_date} au {tournament.end_date}"""
        str += f"""
                        Ce tournoi se déroulera en {tournament.turns} tours avec un contrôle du tems de type {tournament.time_control}"""
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
        return str
