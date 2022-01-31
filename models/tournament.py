from datetime import date, datetime, timedelta
from .dbconnect import DbConnect




class Tournament:
    """Class en charge de la gestion des tournois"""

    def __init__(self, name, place, start_date, end_date,
                 turns, players, time_control,
                 description):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.turns = turns
        self.players = players
        self.time_control = time_control
        self.description = description
        self.duration = (self.end_date - self.start_date + timedelta(1)).days

        db = DbConnect()

        db.db_tournament.insert({
            'name': self.name,
            'place': self.place,
            'start_date': str(self.start_date),
            'end_date': str(self.end_date),
            'turns': self.turns,
            'players': self.players,
            'time_control': self.time_control,
            'description': self.description,
            'duration': self.duration,
        })

    def add_player(self, player):
        if not isinstance(object, player):
            return ValueError("Vous ne pouvez ajouter que des objets de type joueurs")
        self.players.append(player)

    def remove_player(self, player):
        index = self.players.index(player)
        del self.players[index]


