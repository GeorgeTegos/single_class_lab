class Student:

    def __init__(self,name,cohort):
        self.name = name
        self.cohort = cohort
    
    def talk():
        return "I can talk"
    
    def say_favourite_language(self,favourite_language):
        return ("I love " +favourite_language)
    
person1 = Student("george",'e65')

print(person1.say_favourite_language("Python"))


# ---------------------------
# |   Student               |
# ---------------------------
# |   players = list        |
# |   cohoart = str         |
# --------------------------
# |   talk()                |
# |say_favourite_language() |
# ---------------------------