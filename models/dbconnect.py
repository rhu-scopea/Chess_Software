from tinydb import TinyDB, Query
from tinydb.table import Document
from operator import attrgetter


def sorted_by(dict_to_sort, keys):
    """
    Sort a dictionary with one or more attributes
    :param dict_to_sort:
    :param keys: List[tuples]
    :return: Dictionary
    """
    for key in reversed(keys):
        if type(key) is tuple:
            if key[1]:
                dict_to_sort = sorted(dict_to_sort, key=lambda item: item[key[0]], reverse=True)
            else:
                dict_to_sort = sorted(dict_to_sort, key=lambda item: item[key[0]])
        else:
            dict_to_sort = sorted(dict_to_sort, key=lambda item: item[key])

    return dict_to_sort


class DbConnect:
    """Class en charge de la gestion de la Database"""

    def __init__(self):
        self.db_player = TinyDB('./datas/db_player.json', sort_keys=True, indent=4, separators=(',', ': '))
        self.db_player.default_table_name = 'player'

        self.db_tournament = TinyDB('./datas/db_tournament.json', sort_keys=True, indent=4, separators=(',', ': '))
        self.db_tournament.default_table_name = 'tournament'

        self.db_match = TinyDB('./datas/db_match.json', sort_keys=True, indent=4, separators=(',', ': '))
        self.db_match.default_table_name = 'match'

    def get_all_tournaments(self, keys=None):
        if keys:
            return sorted_by(self.db_tournament.all(), keys)
        return self.db_tournament.all()

    def get_tournament_in_progress(self, keys=None):
        query = Query()
        tournaments = self.db_tournament.search(query.status != "Fini")
        if keys:
            return sorted_by(tournaments, keys)

        return tournaments

    def get_all_players(self, keys=None):
        if keys:
            return sorted_by(self.db_player.all(), keys)
        return self.db_player.all()

    def get_list_of_players(self, list_of_players, keys=None):
        players = []
        for player in list_of_players:
            players.append(self.db_player.get(player))
        if keys:
            players = sorted_by(players, keys)
        return players

    def get_all_matches(self):
        return self.db_match.all()

    def edit_player(self, player_id, key, value):
        self.db_player.upsert(Document({key: value}, doc_id=player_id))

    def edit_tournament(self, tournament_id, key, value):
        self.db_tournament.upsert(Document({key: value}, doc_id=tournament_id))
