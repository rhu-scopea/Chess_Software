from tinydb import TinyDB

GENDER = [
    "Homme",
    "Femme",
    "Autre",
]


class Player:
    """Class en charge de la gestion des joueurs"""
    db_player = TinyDB('./datas/db_player.json')
    db_player.default_table_name = 'player'

    def __init__(self, first_name, last_name, date_of_birth, gender, ranking=0, db_player=db_player):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        if ranking < 0:
            return ValueError("Le ranking doit être positif")
        self.ranking = ranking

        self.id = len(db_player) + 1

        db_player.insert({
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'date_of_birth': str(self.date_of_birth),
            'gender': self.gender,
            'ranking': self.ranking,
        })

    @staticmethod
    def get_all_players(db_player=db_player):
        return db_player.all()


    def modify_ranking(self, ranking):
        if ranking < 0:
            return ValueError("Le ranking doit être positif")
        self.ranking = ranking
