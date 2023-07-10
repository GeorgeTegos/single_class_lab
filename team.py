class Team:

    def __init__(self,name,players,coach):
        self.name = name
        self.players = list(players)
        self.coach = coach
        self.points = 0

    def add_player(self,name):
        self.players.append(name)
    
    def has_player(self,name):
        if name in self.players:
            return True
        else:
            return False

    def play_game(self,result):
        if result == True:
            self.points += 3
            

player1 = Team("paok",["george",'bill'],"nick")

print(player1.has_player("george"))


# --------------------
# |   Team |         |
# --------------------
# |   name = str     |
# |   players = list |
# |   coach = str    |
# --------------------
# |   add_player()   |
# |   has_player()   |
# --------------------