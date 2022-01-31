#! /usr/bin/env python3
# coding: utf-8
from typing import List
from datetime import date, datetime, timedelta

from models.player import GENDER
from views import View
from models import Tournament, Player, Match, DbConnect

TIME_CONTROL = (
    "bullet",
    "blitz",
    "coup rapide",
)

DEFAULT_TURNS = 4

NOW = datetime.now()
TODAY = date.today()

class Controller:
    """Main controller."""

    def __init__(self):
        self.view = View()
        self.db = DbConnect()

    def run(self):
        """
        First fonction launch by the controller to show the menu and get the input.
        :return: The choosen menu
        """
        self.view.prompt_menu()
        menu_choice = self.view.ask_input("Veuillez saisir le numéro correspondant à votre choix", '[1-6]', True)

        switcher = {
            '1': self.start_tournament,
            '2': self.show_tournaments,
            '3': self.edit_tournament,
            '4': self.create_player,
            '5': self.show_players,
            '6': self.edit_player,
        }

        # Get the function from switcher dictionary
        func = switcher.get(menu_choice, lambda: print("Good Bye !"))
        # Execute the function
        func()
        self.run()

    def start_tournament(self):
        """
        Ask all the inputs to init the tournament
        :return:
        """
        args = {}
        tournament_name = self.view.ask_input("Nom du tournoi ?", required=True)
        args["name"] = tournament_name
        tournament_place = self.view.ask_input("Emplacement du tournoi ?", required=True)
        args["place"] = tournament_place

        tournament_start = self.view.ask_input("Date de début du tournoi ? (au format jj/mm/aaaa)", "date")
        args["start_date"] = tournament_start or TODAY

        tournament_end = self.view.ask_input("Date de fin du tournoi ? (au format jj/mm/aaaa)", "date")
        if tournament_end >= args['start_date']:
            args["end_date"] = tournament_end
        else:
            args["end_date"] = args['start_date']

        tournament_turns = self.view.ask_input("Nombre de tours ?", "integer")
        args["turns"] = tournament_turns or DEFAULT_TURNS

        tournament_players = self.add_players()
        args["players"] = tournament_players

        list_regex = f"^[1-{len(TIME_CONTROL)}]*$"
        tournament_time_control = int(self.view.ask_input(
            self.view.get_list_to_print(TIME_CONTROL, "Méthode de gestion de controle de temps ?"),
            list_regex)) - 1
        args["time_control"] = TIME_CONTROL[tournament_time_control] or TIME_CONTROL[0]

        tournament_description = self.view.ask_input("Veuillez saisir la description du tournoi")
        args["description"] = tournament_description or None

        tournament = Tournament(**args)
        self.view.show_tournament(tournament)

        input()

    def show_tournaments(self):
        tournaments = self.db.get_all_tournaments()
        self.view.show_all_tournaments(tournaments)
        input()

    def edit_tournament(self):
        tournaments = Tournament.get_all_tournaments()

        list_regex = f"^[1-{len(tournaments)}]*$"
        tournament_choice = \
            int(
                self.view.ask_input(
                    self.view.get_list_to_print(
                        tournaments, "Veuillez choisir la méthode de gestion de controle de temps"),
                    list_regex)
            ) - 1
        if tournament_choice:
            print(tournaments[tournament_choice])

    def add_players(self):

        tournament_players = []
        input_player = True
        while input_player:
            players = self.db.get_all_players()
            if tournament_players:
                print("\nJoueurs actuellement selectionnés :")
                self.view.show_players(players, include=tournament_players)

            print("\nJoueurs selectionnables :")
            self.view.show_players(players, exception=tournament_players)
            input_player = self.view.ask_input(
                "Choisissez le numéro d'un joueur\nLaisser vide pour passer à la section suivante\nou tappez 0 pour créer un nouveau joueur",
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

        return tournament_players

    def create_player(self):
        """
        Ask all the inputs to create a new player
        :return:
        """
        args = {}
        player_fist_name = self.view.ask_input("Prénom du joueur ?", required=True)
        args["first_name"] = player_fist_name
        player_last_name = self.view.ask_input("Nom du joueur ?", required=True)
        args["last_name"] = player_last_name

        player_date_of_birth = self.view.ask_input("Date de naissance du joueur ? (au format jj/mm/aaaa)", "date", required=True)
        args["date_of_birth"] = player_date_of_birth

        player_gender = self.view.ask_input_on_list("Genre du joueur ?", GENDER, required=True)
        args["gender"] = player_gender

        player_ranking = self.view.ask_input("Rang du joueur ?", "[0-9]*")
        args["ranking"] = int(player_ranking) or 0

        player = Player(**args)
        self.view.show_player(player)

        input()


    def show_players(self):
        players = self.db.get_all_players()
        self.view.show_players(players)

        input()

    def edit_player(self):

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
                        player_change = self.view.ask_input_on_list("Caractérisitque à modifier ?", list(player.keys()), required=True)
                        print(player[player_change])
                        break

