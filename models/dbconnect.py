from tinydb import TinyDB


def multikeysort(items, columns):
    """
    Fonction to sort dictionaries with one or many columns condition
    :param items: Dictionary
    :param columns: List of columns
    :return: Dictionary
    to sort in descending order put "-" before the name of the column
    ex : result = multikeysort(undecorated, ['-key1', '-key2', 'key3'])
    """
    from operator import itemgetter
    comparers = [((itemgetter(col[1:].strip()), -1) if col.startswith('-') else (itemgetter(col.strip()), 1)) for col in columns]

    def comparer(left, right):
        for fn, mult in comparers:
            result = cmp(fn(left), fn(right))
            if result:
                return mult * result
        else:
            return 0

    return sorted(items, cmp=comparer)

    def cmp(a, b):
        return (a > b) - (a < b)


class DbConnect:
    """Class en charge de la gestion de la Database"""

    def __init__(self):
        self.db_player = TinyDB('./datas/db_player.json', sort_keys=True, indent=4, separators=(',', ': '))
        self.db_player.default_table_name = 'player'

        self.db_tournament = TinyDB('./datas/db_tournament.json', sort_keys=True, indent=4, separators=(',', ': '))
        self.db_tournament.default_table_name = 'tournament'

        self.db_match = TinyDB('./datas/db_match.json')
        self.db_match.default_table_name = 'match'

    def get_all_tournaments(self, columns=None):
        if columns:
            return multikeysort(self.db_tournament.all(), columns)
        return self.db_tournament.all()

    def get_all_players(self, columns=None):
        if columns:
            return multikeysort(self.db_player.all(), columns)
        return self.db_player.all()

    def get_all_matches(self):
        return self.db_match.all()

    def edit_player(self, key):
        self.db_player

    