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
        self.start_tournament()
        menu_choice = self.view.prompt_menu()

        switcher = {
            '1': self.start_tournament,
            '2': self.start_tournament,
            '3': self.start_tournament,
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
        tournament_name = self.view.ask_input("Veuillez saisir le nom du tournoi")
        if not tournament_name:
            return
        tournament_place = self.view.ask_input("Veuillez saisir l'emplacement du tournoi")
        if not tournament_place:
            return
        tournament_start = self.view.ask_input("Veuillez la date de début du tournoi", constraint_type='date')
        tournament_end = self.view.ask_input("Veuillez la date de fin du tournoi", constraint_type='date')
        tournament_turns = self.view.ask_input("Nombre de tours ?", '^[0-9]*$')

        tournament_time_control = self.view.ask_input(
            self.view.get_list_to_print(TIME_CONTROL, "Veuillez choisir la méthode de gestion de controle de temps"),
            '^[0-9]*$')
        tournament_description = self.view.ask_input("Veuillez saisir la description du tournoi")

        tournament = Tournament(
            tournament_name,
            tournament_place,
            tournament_start,
            tournament_end,
            tournament_turns,
            [],
            tournament_time_control,
            tournament_description
        )
        self.view.show_tournament(tournament)

        # args = self.view.prompt_for_new_tournament()
        # print(args)
        # tournament_view = TournamentView(tournament)
        # print(tournament_view.show_tournament())

    def add_player(self):
        pass

