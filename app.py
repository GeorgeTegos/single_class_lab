from students import *
from team import *

person1 = Student("george",'e65')
print(person1.say_favourite_language("Python"))

print("\n\n")


player1 = Team("paok",["george","josh"],"nick")

print(player1.has_player("george"))
player1.add_player("bill")

print(player1.players)