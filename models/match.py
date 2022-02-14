from .dbconnect import DbConnect


class Match:
    def __init__(self, player_1, player_2, score_p1, score_p2, turn, tournament, start_time, end_time):
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_p1 = score_p1
        self.score_p2 = score_p2
        self.turn = turn
        self.tournament = tournament
        self.start_time = start_time
        self.end_time = end_time

        db = DbConnect()

        db.db_match.insert({
            'player_1': self.player_1,
            'player_2': self.player_2,
            'score_p1': self.score_p1,
            'score_p2': self.score_p2,
            'turn': self.turn,
            'tournament': self.tournament,
            'start_time': str(self.start_time),
            'end_time': str(self.end_time),
        })
