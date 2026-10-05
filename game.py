class Game:
    def __int__ (self, team1, team2):
        self.team1 = team1
        self.team2 = team2

        self.quarter = 1
        self.overtime = False
        self.away = False  #is the game played at home or not

        self.team1Score = 0;
        self.team2Score = 0;

