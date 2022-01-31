from .dbconnect import DbConnect

GENDER = [
    "Homme",
    "Femme",
    "Autre",
]


class Player:
    """Class en cherche de la gestion des joueurs"""

    def __init__(self, first_name, last_name, date_of_birth, gender, ranking):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking

        db = DbConnect()

        db.db_player.insert({
            'first_name': self.first_name,
            'last_name': self.last_name,
            'date_of_birth': str(self.date_of_birth),
            'gender': self.gender,
            'ranking': self.ranking,
        })

    def modify_ranking(self, ranking):
        if ranking < 0:
            return ValueError("Le ranking doit être positif")
        self.ranking = ranking
