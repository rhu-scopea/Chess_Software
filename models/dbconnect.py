import re

from tinydb import TinyDB, Query
from tinydb.table import Document
import operator
import typing


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
            players.append(self.db_player.get(doc_id=player))
        if keys:
            players = sorted_by(players, keys)
        return players

    def get_all_matches(self):
        return self.db_match.all()

    def edit_player(self, player_id, key, value):
        self.db_player.upsert(Document({key: value}, doc_id=player_id))

    def edit_tournament(self, tournament_id, key, value):
        self.db_tournament.upsert(Document({key: value}, doc_id=tournament_id))

    def get_players_scores(self, tournament_id):
        query = Query()
        matches = self.db_match.search(query.tournament == tournament_id)

        players_scores = {}
        for match in matches:
            p1 = match['player_1']
            if p1 in players_scores.keys():
                players_scores[p1]['score'] += match['score_p1']
            else:
                players_scores[p1] = {}
                players_scores[p1]['score'] = match['score_p1']

            p2 = match['player_2']
            if p2 in players_scores.keys():
                players_scores[p2]['score'] += match['score_p2']
            else:
                players_scores[p2] = {}
                players_scores[p2]['score'] = match['score_p2']

        players = self.get_list_of_players(players_scores.keys())
        for player in players:
            players_scores[player.doc_id]['ranking'] = player['ranking']
            players_scores[player.doc_id]['name'] = player['first_name'] + ' ' + player['last_name']

        players_scores = dict(sorted(players_scores.items(), key=lambda x: (x[1]['score'], x[1]['ranking']), reverse=True))

        return players_scores

    def get_match_played(self, tournament_id: int, player_id: int, players_ids: list):
        query = Query()
        matches = self.db_match.search((query.tournament == tournament_id) & ((query.player_1 == player_id) | (query.player_2 == player_id)))
        matches_played = {}
        if len(players_ids) == 1:
            players_ids = list(players_ids)
        for player in players_ids:
            matches_played[player] = 0

        for match in matches:
            if match['player_1'] == player_id:
                player_num = match['player_2']
            else:
                player_num = match['player_1']
            if player_num in matches_played.keys():
                matches_played[player_num] += 1

        no_match = [p for p in matches_played if matches_played[p] == 0]

        return no_match
