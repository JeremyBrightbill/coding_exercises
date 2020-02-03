"""Program to evenly divide pizzas. Prompts for number of people, number of 
pizzas, and number of slices per pizza. Ensures that the number of slices per 
person comes out even. Displays the number of pieces each person should get, 
plus any remainder.

Challenge: Allow only numeric input. Handle pluralization (piece vs. pieces).

WORK IN PROGRESS"""

class Event():

    def __init__(self, people: int, pizzas: int, pieces: int): 
        self.people = people
        self.pizzas = pizzas
        self.pieces = pieces
        self.per_person = (self.pizzas * self.pieces) // self.people
        self.remainder = (self.pizzas * self.pieces) % self.people
    
    def __repr__(self): 
        return \
f"""{self.people} people with {self.pizzas} pizzas, {self.pieces} slices per pizza. 
Each person gets {self.per_person} slices of pizza. 
There are {self.remainder} slices left over."""

if __name__ == "__main__":
    event = Event(3, 4, 13)
    print(event)