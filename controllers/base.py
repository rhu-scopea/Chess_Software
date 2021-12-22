#! /usr/bin/env python3
# coding: utf-8

from typing import List

from views import View, TournamentView
from models import Tournament, Player


class Controller:
    """Main controller."""

    def __init__(self, view: View):
        self.view = view

    def start_tournament(self):
        args = self.view.prompt_for_new_tournament()
        print(args)
        tournament = Tournament(args["name"], args["place"])
        tournament_view = TournamentView(tournament)
        print(tournament_view.show_tournament())

    def run(self):
        self.start_tournament()
