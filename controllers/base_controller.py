#! /usr/bin/env python3
# coding: utf-8

from typing import List

from views import View, TournamentView
from models import Tournament, Player, Match


class Controller:
    """Main controller."""

    def __init__(self):
        self.view = View()

    def start_tournament(self):
        print("Merci d'avoir créé un tournoi")
        # args = self.view.prompt_for_new_tournament()
        # print(args)
        # tournament = Tournament(args)
        # tournament_view = TournamentView(tournament)
        # print(tournament_view.show_tournament())

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

