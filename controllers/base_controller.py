#! /usr/bin/env python3
# coding: utf-8
import datetime
from typing import List

from models.tournament import TIME_CONTROL
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
        # self.show_tournament()
        menu_choice = self.view.prompt_menu()

        switcher = {
            '1': self.start_tournament,
            '2': self.edit_tournament,
            '3': self.show_tournament,
            '4': self.start_tournament,
            '5': self.start_tournament,
        }

        # Get the function from switcher dictionary
        func = switcher.get(menu_choice, lambda: "Good Bye !")
        # Execute the function
        print(func())

    def start_tournament(self):
        """
        Ask all the inputs to init the tournament
        :return:
        """
        args = {}
        tournament_name = self.view.ask_input("Veuillez saisir le nom du tournoi", required=True)
        args["name"] = tournament_name
        tournament_place = self.view.ask_input("Veuillez saisir l'emplacement du tournoi", required=True)
        args["place"] = tournament_place

        tournament_start = self.view.ask_input("Veuillez la date de début du tournoi", "date")
        if tournament_start:
            args["start_date"] = tournament_start

        tournament_end = self.view.ask_input("Veuillez la date de fin du tournoi", "date")
        if tournament_end:
            args["end_date"] = tournament_end

        tournament_turns = self.view.ask_input("Nombre de tours ?", "integer")
        if tournament_turns:
            args["turns"] = tournament_turns

        list_regex = f"^[1-{len(TIME_CONTROL)}]*$"
        tournament_time_control = self.view.ask_input(
            self.view.get_list_to_print(TIME_CONTROL, "Veuillez choisir la méthode de gestion de controle de temps"),
            list_regex) - 1
        if tournament_time_control:
            args["time_control"] = TIME_CONTROL[tournament_time_control]

        tournament_description = self.view.ask_input("Veuillez saisir la description du tournoi")
        if tournament_description:
            args["description"] = tournament_description

        tournament = Tournament(**args)
        self.view.show_tournament(tournament)

    def edit_tournament(self, tournament):
        print("Yolo")

    def show_tournament(self):
        tournaments = Tournament.get_all_tournaments()
        self.view.show_all_tournaments(tournaments)

    def add_player(self):
        pass
