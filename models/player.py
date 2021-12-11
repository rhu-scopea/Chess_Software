

class Player:
    def __init__(self, first_name, last_name, date_of_birth, gender, ranking=0):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        if ranking < 0:
            return ValueError("Le ranking doit être positif")
        self.ranking = ranking

    def modify_ranking(self, ranking):
        if ranking < 0:
            return ValueError("Le ranking doit être positif")
        self.ranking = ranking


