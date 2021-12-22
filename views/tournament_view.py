#! /usr/bin/env python3
# coding: utf-8
from models.tournament import Tournament


class TournamentView:
    def __init__(self, tournament: Tournament):
        self.tournament = tournament

    def show_tournament(self):
        str = f"""
                        Le tournoi {self.tournament.name}, prendra place à {self.tournament.place} """
        if self.tournament.duration == 1:
            str += f"""la journée du {self.tournament.start_date} """
        else:
            str += f"""du {self.tournament.start_date} au {self.tournament.end_date}"""
        str += f"""
                        Ce tournoi se déroulera en {self.tournament.turns} tours avec un contrôle du tems de type {self.tournament.time_control}"""
        if self.tournament.description:
            str += f"""
                        *****************************************************        
                        Description du Tournoi :
                        {self.tournament.description}
                        """
        if self.tournament.players:
            str += f"""
                        *****************************************************
                        Joueurs :
                    """
            for player in self.tournament.players:
                str += f"\n{player}"
        return str