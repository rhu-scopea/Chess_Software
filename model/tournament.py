from datetime import date, datetime

TIME_CONTROL = (
    "bullet",
    "blitz",
    "coup rapide",
)

DEFAULT_TURNS = 4

NOW = datetime.datetime.now()
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
        self.duration = self.end_date - self.start_date + 1

    def __str__(self):
        str = f"""Le tournoi {self.name}, prendra place à {self.place} """
        if self.duration == 1 :
            str += f"""la journée du {self.start_date} """
        else:
            str += f"""du {self.start_date} au {self.end_date}"""
        str += f"""\nCe tournoi se déroulera en {self.turns} avec un contrôle du temps de type {self.time_control}
                
                *****************************************************        
                Description du Tournoi :
                {self.description}
                
                *****************************************************
                Joueurs :
                """


