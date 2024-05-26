
class Stats():
    def __init__(self):
        self.p1_score = 0
        self.p2_score = 0
        self.draws = 0
        self.games_played = 0

    def reset(self):
        self.p1_score = 0
        self.p2_score = 0
        self.draws = 0
        self.games_played = 0

    def update_winner(self, winner):
        if winner == 1:
            self.p1_score += 1
        elif winner == 2:
            self.p2_score += 1
        self.games_played += 1

    def update_draws(self):
        self.draws += 1
        self.games_played += 1


