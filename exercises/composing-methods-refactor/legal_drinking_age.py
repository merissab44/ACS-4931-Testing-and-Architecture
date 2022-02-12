# by Kami Bigdely
# Inline method.
# TODO: Refactor this program to improve its readability.

LEGAL_DRINKING_AGE = 18
class Person:
    def __init__(self, my_age):
        self.age = my_age
        
def enter_night_club(individual):
    print("Allowed to enter.") if individual.age >= LEGAL_DRINKING_AGE else print("Enterance of minors is denited.")
    
    
person = Person(23)
enter_night_club(person)
        
