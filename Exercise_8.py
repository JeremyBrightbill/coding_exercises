"""Program to evenly divide pizzas. Prompts for number of people, number of 
pizzas, and number of slices per pizza. Ensures that the number of slices per 
person comes out even. Displays the number of pieces each person should get, 
plus any remainder.

Challenge: Handle pluralization (piece vs. pieces)."""

import inflect

p = inflect.engine()

class Event():

    def __init__(self, people: int, pizzas: int, pieces: int): 
        self.people = people
        self.pizzas = pizzas
        self.pieces = pieces
        self.per_person = (self.pizzas * self.pieces) // self.people
        self.remainder = (self.pizzas * self.pieces) % self.people
    
    # Using inflect module, conditionally form plural based on number
    def __repr__(self): 
        return \
f"""{self.people} {p.plural("person", self.people)} with {self.pizzas} {p.plural("pizza", self.pizzas)}, \
{self.pieces} {p.plural("slice", self.pieces)} per pizza. 
Each person gets {self.per_person} {p.plural("slice", self.per_person)} of pizza. 
There {p.plural_verb("is", self.remainder)} {self.remainder} {p.plural("slice", self.remainder)} left over."""

if __name__ == "__main__":
    event = Event(2, 1, 3)
    print(event)