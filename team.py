class Team:

    def __init__(self,name,players,coach):
        self.name = name
        self.players = players
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
        if result == True or "won":
            self.points += 3
            

# player1 = Team("paok",["george","josh"],"nick")

# print(player1.has_player("george"))
# player1.add_player("bill")

# print(player1.players)


# ---------------------
# |   Team            |
# ---------------------
# |   name = str      |
# |   players = list  |
# |   coach = str     |
# ---------------------
# |add_player(name)   |
# |play_game(result)  |
# | True / False      |
# |has_player(name)   |
# | True / False      |
# ---------------------