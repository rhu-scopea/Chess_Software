#! /usr/bin/env python3
# coding: utf-8
import datetime
from typing import List

from models.tournament import TIME_CONTROL
from models.player import GENDER
from views import View
from models import Tournament, Player, Match


class Controller:
    """Main controller."""

    def __init__(self):
        self.view = View()

    def run(self):
        """
        First fonction launch by the controller to show the menu and get the input.
        :return: The choosen menu
        """
        # self.show_tournaments()
        menu_choice = self.view.prompt_menu()

        switcher = {
            '1': self.date_of_birth_tournament,
            '2': self.show_tournaments,
            '3': self.edit_tournament,
            '4': self.create_player,
            '5': self.show_players,
        }

        # Get the function from switcher dictionary
        func = switcher.get(menu_choice, lambda: "Good Bye !")
        # Execute the function
        print(func())

    def date_of_birth_tournament(self):
        """
        Ask all the inputs to init the tournament
        :return:
        """
        args = {}
        tournament_name = self.view.ask_input("Veuillez saisir le nom du tournoi", required=True)
        args["name"] = tournament_name
        tournament_place = self.view.ask_input("Veuillez saisir l'emplacement du tournoi", required=True)
        args["place"] = tournament_place

        tournament_start = self.view.ask_input("Veuillez saisir la date de début du tournoi", "date")
        if tournament_start:
            args["start_date"] = tournament_start

        tournament_end = self.view.ask_input("Veuillez saisir la date de fin du tournoi", "date")
        if tournament_end:
            args["end_date"] = tournament_end

        tournament_turns = self.view.ask_input("Nombre de tours ?", "integer")
        if tournament_turns:
            args["turns"] = tournament_turns

        list_regex = f"^[1-{len(TIME_CONTROL)}]*$"
        tournament_time_control = int(self.view.ask_input(
            self.view.get_list_to_print(TIME_CONTROL, "Veuillez choisir la méthode de gestion de controle de temps"),
            list_regex)) - 1
        if tournament_time_control:
            args["time_control"] = TIME_CONTROL[tournament_time_control]

        tournament_description = self.view.ask_input("Veuillez saisir la description du tournoi")
        if tournament_description:
            args["description"] = tournament_description

        tournament = Tournament(**args)
        self.view.show_tournament(tournament)

    def show_tournaments(self):
        tournaments = Tournament.get_all_tournaments()
        self.view.show_all_tournaments(tournaments)

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

    def add_player(self):
        pass

    def create_player(self):
        """
        Ask all the inputs to create a new player
        :return:
        """
        args = {}
        player_fist_name = self.view.ask_input("Veuillez saisir le prénom du joueur", required=True)
        args["first_name"] = player_fist_name
        player_last_name = self.view.ask_input("Veuillez saisir le nom du joueur", required=True)
        args["last_name"] = player_last_name

        player_date_of_birth = self.view.ask_input("Veuillez saisir la date de naissance du joueur", "date", required=True)
        args["date_of_birth"] = player_date_of_birth

        player_gender = self.view.ask_input_on_list("Veuillez choisir le genre du joueur", GENDER, required=True)
        args["gender"] = player_gender

        player_ranking = self.view.ask_input("Veuillez saisir le rang du joueur", "integer")
        if player_ranking:
            args["ranking"] = player_ranking

        player = Player(**args)
        self.view.show_player(player)

    def show_players(self):
        tournaments = Tournament.get_all_tournaments()
        self.view.show_all_tournaments(tournaments)
