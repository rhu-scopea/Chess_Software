#! /usr/bin/env python3
# coding: utf-8

from typing import List

from models.tournament import Tournament
from models.player import Player


class Controller:
    """Main controller."""

    def __init__(self, tournament: Tournament):
        self.tournament = tournament

    def run(self):
        pass


