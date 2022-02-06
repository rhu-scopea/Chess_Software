#! /usr/bin/env python3
# coding: utf-8
from typing import List

from models.constants import *
from views import View
from models import Tournament, Player, Match, DbConnect


class Controller:
    """Main controller."""

    def __init__(self):
        self.view = View()
        self.db = DbConnect()

    def run(self):
        """
        First fonction launch by the controller to show the menu and get the input.
        :return: function
        """
        self.view.prompt_menu()
        menu_choice = self.view.ask_input("Veuillez saisir le numéro correspondant à votre choix", '[1-7]', True)

        switcher = {
            '1': self.start_tournament,
            '2': self.start_match,
            '3': self.show_tournaments,
            '4': self.edit_tournament,
            '5': self.create_player,
            '6': self.show_players,
            '7': self.edit_player,
        }

        # Get the function from switcher dictionary
        func = switcher.get(menu_choice, lambda: print("Good Bye !"))
        # Execute the function
        func()
        self.run()

    def set_tournament_name(self):
        return self.view.ask_input("Nom du tournoi ?", required=True)

    def set_tournament_place(self):
        return self.view.ask_input("Emplacement du tournoi ?", required=True)

    def set_tournament_start_date(self):
        return self.view.ask_input("Date de début du tournoi ? (au format jj/mm/aaaa)", "date") or TODAY

    def set_tournament_end_date(self, start_date):
        end_date = self.view.ask_input("Date de fin du tournoi ? (au format jj/mm/aaaa)", "date")
        if end_date >= start_date:
            return end_date
        else:
            return start_date

    def set_tournament_turns(self):
        return self.view.ask_input("Nombre de tours ?", "integer") or DEFAULT_TURNS

    def set_tournament_time_control(self):
        list_regex = f"^[1-{len(TIME_CONTROL)}]*$"
        tournament_time_control = int(self.view.ask_input(
            self.view.get_list_to_print(TIME_CONTROL, "Méthode de gestion de controle de temps ?"),
            list_regex)) - 1
        return TIME_CONTROL[tournament_time_control] or TIME_CONTROL[0]

    def set_tournament_description(self):
        return self.view.ask_input("Veuillez saisir la description du tournoi") or None

    def start_tournament(self):
        """
        Ask all the inputs to init the tournament
        :return:
        """
        args = {}
        args["name"] = self.set_tournament_name()
        args["place"] = self.set_tournament_place()
        args["start_date"] = self.set_tournament_start_date()
        args["end_date"] = self.set_tournament_end_date(args["start_date"])
        args["turns"] = self.set_tournament_turns()
        args["players"] = self.assign_players()
        args["time_control"] = self.set_tournament_time_control()
        args["description"] = self.set_tournament_description()

        tournament = Tournament(**args)
        self.view.show_tournament(tournament)

        input()

    def start_match(self):
        """
        Ask all the inputs to init the match
        :return:
        """
        tournaments = self.db.get_tournament_in_progress(['name'])
        self.view.show_tournaments(tournaments)
        tournament = self.select_tournament(tournaments, "Selectionnez le tournoi à lancer")

        if tournament["status"] == 'Doit commencer':
            self.first_match(tournament)
        input()

    def first_match(self, tournament):
        players = self.db.get_list_of_players(tournament["players"], [('ranking', 1)])

    def select_tournament(self, tournaments, message=""):
        input_tournament = None
        while not input_tournament:
            self.view.show_tournaments(tournaments)

            input_tournament = self.view.ask_input(
                message,
                "integer"
            )
            if input_tournament:
                for tournament in tournaments:
                    if tournament.doc_id == input_tournament:
                        return tournament

    def show_tournaments(self):
        """
        Fonction to display all the tournaments
        :return: None
        """
        tournaments = self.db.get_all_tournaments()
        self.view.show_tournaments(tournaments)
        input()

    def edit_tournament(self):
        """
        Fonction to edit the tournament after asking which field to change
        :return: None
        """
        tournaments = self.db.get_all_tournaments()
        input_tournament = None
        while not input_tournament:
            self.view.show_tournaments(tournaments)

            input_tournament = self.view.ask_input(
                "Tournoi à modifier ?",
                "integer"
            )
            if input_tournament:
                for tournament in tournaments:
                    if tournament.doc_id == input_tournament:
                        tournament_key = self.view.ask_input_on_list("Caractérisitque à modifier ?", list(tournament.keys()), required=True)

                        func = self.set_tournament(tournament_key)
                        if tournament_key == "end_date":
                            tournament_value = func(tournament["start_date"])
                        elif  tournament_key == "players":
                            tournament_value = func(tournament)
                        else:
                            tournament_value = func()
                        self.db.edit_tournament(tournament.doc_id, tournament_key, tournament_value)
                        break
        self.show_tournaments()

    def set_tournament(self, key):
        """
        Get the function to edit a tournamet field, called by the function tournament_edit()
        :param key:
        :return: function
        """
        switcher = {
            "name": self.set_tournament_name,
            "place": self.set_tournament_place,
            "start_date": self.set_tournament_start_date,
            "end_date": self.set_tournament_end_date,
            "turns": self.set_tournament_turns,
            "players": self.assign_players,
            "time_control": self.set_tournament_time_control,
            "description": self.set_tournament_description
        }
        return switcher.get(key, lambda: print("Not working"))

    def assign_players(self, tournament=None):
        """
        Function to assign or delete players from tournament
        :param tournament: Tournament()
        :return: List
        """
        if tournament:
            tournament_players = tournament['players']
        else:
            tournament_players = []
        input_player = True
        while input_player and len(tournament_players) != 8:
            players = self.db.get_all_players()
            if tournament_players:
                print("\nJoueurs actuellement selectionnés : (il faut 8 joueurs)")
                self.view.show_players(players, include=tournament_players)

            print("\nJoueurs selectionnables :")
            self.view.show_players(players, exception=tournament_players)
            input_player = self.view.ask_input(
                "Tappez le numéro d'un joueur pour l'ajouter\nTappez le numéro d'un joueur avec un - devant pour l'enlever\nLaisser vide pour passer à la section suivante\nou tappez 0 pour créer un nouveau joueur",
                "integer"
            )
            if input_player == 0:
                self.create_player()
                input_player = True
            elif input_player:
                for player in players:
                    if player.doc_id == input_player:
                        if player.doc_id not in tournament_players:
                            tournament_players.append(player.doc_id)
                            break
                        else:
                            print('Joueur déja sélectionné')
                    elif player.doc_id == (input_player * -1):
                        if player.doc_id in tournament_players:
                            tournament_players.remove(player.doc_id)
                            break
                        else:
                            print("Joueur n'est pas encore sélectionné")


        return tournament_players

    def set_player_first_name(self):
        return self.view.ask_input("Prénom du joueur ?", required=True)

    def set_player_last_name(self):
        return self.view.ask_input("Nom du joueur ?", required=True)

    def set_player_date_of_birth(self):
        return self.view.ask_input("Date de naissance du joueur ? (au format jj/mm/aaaa)", "date", required=True)

    def set_player_gender(self):
        return self.view.ask_input_on_list("Genre du joueur ?", GENDER, required=True)

    def set_player_ranking(self):
        player_ranking = self.view.ask_input("Rang du joueur ?", "[0-9]*")
        return int(player_ranking) or 0

    def create_player(self):
        """
        Ask all the inputs to create a new player
        :return: None
        """
        args = {
            "first_name": self.set_player_first_name(),
            "last_name": self.set_player_last_name(),
            "date_of_birth": self.set_player_date_of_birth(),
            "gender": self.set_player_gender(),
            "ranking": self.set_player_ranking()
        }

        player = Player(**args)
        self.view.show_player(player)

        input()

    def show_players(self):
        """
        Function to display all the players
        :return: None
        """
        players = self.db.get_all_players()
        self.view.show_players(players)

        input()

    def edit_player(self):
        """
        Fonction to edit the player after asking which field to change
        :return: None
        """
        players = self.db.get_all_players()
        input_player = None
        while not input_player:
            self.view.show_players(players)

            input_player = self.view.ask_input(
                "Joueur à modifier ?",
                "integer"
            )
            if input_player:
                for player in players:
                    if player.doc_id == input_player:
                        player_key = self.view.ask_input_on_list("Caractérisitque à modifier ?", list(player.keys()), required=True)

                        func = self.set_player(player_key)
                        player_value = func()
                        self.db.edit_player(player.doc_id, player_key, player_value)
                        break
        self.show_players()

    def set_player(self, key):
        """
        Get the function to edit a player field, called by the function player_edit()
        :param key:
        :return: function
        """
        switcher = {
            'first_name': self.set_player_first_name,
            'last_name': self.set_player_last_name,
            'date_of_birth': self.set_player_date_of_birth,
            'gender': self.set_player_gender,
            'ranking': self.set_player_ranking
        }
        return switcher.get(key, lambda: print("Not working"))
