#! /usr/bin/env python3
# coding: utf-8
import argparse


class View():

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
