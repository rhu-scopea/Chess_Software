from datetime import date, datetime, timedelta

TIME_CONTROL = (
    "bullet",
    "blitz",
    "coup rapide",
)

DEFAULT_TURNS = 4

NOW = datetime.now()
TODAY = date.today()


class Tournament:
    """Class en cherche de la gestion des tournois"""
    def __init__(self, name, place, start_date=TODAY, end_date=TODAY,
                 turns=DEFAULT_TURNS, players=[], time_control=TIME_CONTROL[0],
                 description=None):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.turns = turns
        self.players = players
        self.time_control = time_control
        self.description = description
        self.duration = (self.end_date - self.start_date + timedelta(1)).days

    def add_player(self, player):
        if not isinstance(object, player):
            return ValueError("Vous ne pouvez ajouter que des objets de type joueurs")
        self.players.append(player)

    def remove_player(self, player):
        index = self.players.index(player)
        del self.players[index]

    def __str__(self):
        str = f"""
                Le tournoi {self.name}, prendra place à {self.place} """
        if self.duration == 1:
            str += f"""la journée du {self.start_date} """
        else:
            str += f"""du {self.start_date} au {self.end_date}"""
        str += f"""
                Ce tournoi se déroulera en {self.turns} tours avec un contrôle du temps de type {self.time_control}"""
        if self.description:
            str += f"""
                *****************************************************        
                Description du Tournoi :
                {self.description}
                """
        if self.players:
            str += f"""
                *****************************************************
                Joueurs :
            """
            for player in self.players:
                str += f"\n{player}"
        return str

    def __repr__(self):
        return str(self)


tournoi = Tournament("Galinettes", "Bayonne", "2021-12-20")
print(tournoi)
