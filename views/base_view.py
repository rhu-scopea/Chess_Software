#! /usr/bin/env python3
# coding: utf-8
import argparse
import re

class View():

    def ask_input(self, message, input_constraint='*'):
        """
        Fonction to ask an input and control it with regex
        :param message: Message to show to the user
        :param input_constraint: Regex
        :return: the input if match with the regex
        """
        input_response = None
        check_input = None
        while not input_response or not check_input:
            input_response = input(message + "\n")
            check_input = re.match(input_constraint, input_response)
            if re.match("q|Q", input_response):
                print("Saisie annulée\n")
                return None
            if not check_input:
                print("Merci de faire une saisie correcte")
        return input_response

    def prompt_menu(self):
        print("""
        Bienvenu sur Chess Master Tournament
        
        Veuillez choisir la section désirée :
        1. Créer un tournoi
        2. Editer un tournoi
        3. Afficher les tournois
        4. Créer des joueurs
        5. Afficher les joueurs
        *************************************
        """)
        return self.ask_input("Veuillez saisir le numéro correspondant à votre choix", '[1-5]')






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
