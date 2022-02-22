#! /usr/bin/env python3
# coding: utf-8
import datetime
import operator
import re
from prettytable import PrettyTable


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

        while not input_response and input_response != 0:
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

        if re.match("[qQ]", input_response):
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
                    input_response = datetime.datetime.strptime(input_response, "%d/%m/%Y").date()
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

    def get_list_to_print(self, list_item, message=""):
        message = message + "\n" or message
        num = 0
        for item in list_item:
            num += 1
            message += f"[{num}] : {item}\n"
        return message

    def ask_input_on_list(self, message, input_list, required=False):
        list_regex = f"^[1-{len(input_list)}]*$"
        list_index = int(self.ask_input(
            self.get_list_to_print(input_list, message),
            list_regex, required))
        if list_index:
            return input_list[list_index - 1]
        return

    def prompt_menu(self):
        print("""
        Bienvenu sur Chess Master Tournament
        
        Veuillez choisir la section désirée :
        1. Créer un tournoi
        2. Lancer un round
        3. Afficher les tournois
        4. Editer un tournoi
        5. Afficher les résultats d'un tournoi
        6. Créer un joueur
        7. Afficher les joueurs
        8. Editer un joueur
        *************************************
        """)

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

    def show_tournaments(self, tournaments):
        t = PrettyTable(['id', 'Name', 'Place', 'Start date', 'End date', 'Turns', 'Actual turn', 'Number of players', 'Time control', 'Status'])

        for tournament in tournaments:
            t.add_row(
                [
                    tournament.doc_id,
                    tournament["name"],
                    tournament["place"],
                    tournament["start_date"],
                    tournament["end_date"],
                    tournament["turns"],
                    tournament["active_turn"],
                    len(tournament["players"]),
                    tournament["time_control"],
                    tournament["status"],
                ]
            )
        print(t)

    def show_player(self, player):
        if player.gender == "Femme":
            str = f"""
                Joueuse : {player.first_name} {player.last_name}
                née le : {player.date_of_birth}"""
        else:
            str = f"""
                Joueur : {player.first_name} {player.last_name}
                Né le : {player.date_of_birth}"""

        str += f"""
                Rang : {player.ranking}"""

        print(str)

    def show_players(self, players, sort='name', exception=[], include=[]):
        t = PrettyTable(['N°', 'Prénom', 'Nom', 'Date de naissance', 'Genre', 'Rang'])
        for player in players:
            if include:
                if player.doc_id in include:
                    t.add_row(
                        [
                            player.doc_id,
                            player["first_name"],
                            player["last_name"],
                            player["date_of_birth"],
                            player["gender"],
                            int(player["ranking"]),
                        ]
                    )
            elif player.doc_id not in exception:
                t.add_row(
                    [
                        player.doc_id,
                        player["first_name"],
                        player["last_name"],
                        player["date_of_birth"],
                        player["gender"],
                        int(player["ranking"]),
                    ]
                )
        if sort == 'name':
            print(t.get_string(sort_key=operator.itemgetter(3, 2), sortby="Nom"))
        else:
            print(t.get_string(sortby="Rang", reversesort=True))

    def show_pairs(self, players, pairs):
        t = PrettyTable(['Paire', 'Joueur 1', 'Joueur 2'])

        pair_number = 0
        for pair in pairs:
            pair_number += 1
            nb_player_1 = pair['player_1']
            player_1 = players[nb_player_1]
            display_p1 = player_1['first_name'] + ' ' + player_1['last_name']

            nb_player_2 = pair['player_2']
            player_2 = players[nb_player_2]
            display_p2 = player_2['first_name'] + ' ' + player_2['last_name']

            t.add_row(
                [
                    pair_number,
                    display_p1,
                    display_p2,
                ]
            )
        print(t)

    def display_results(self, players_scores):
        t = PrettyTable(['Joueur', 'Score', 'Classement'])

        for player in players_scores:
            t.add_row(
                [
                    players_scores[player].get('name'),
                    players_scores[player].get('score'),
                    players_scores[player].get('ranking'),
                ]
            )
        print(t)
