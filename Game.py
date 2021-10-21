

class Game:
    def __init__(self, game):
        self.userNum = game['userNum']
        self.gameId = game['gameId']
        self.seasonId = game['seasonId']
        self.startDtm = game['startDtm']
        self.mmrBefore = game['mmrBefore']
