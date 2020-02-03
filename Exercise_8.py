"""Program to evenly divide pizzas. Prompts for number of people, number of 
pizzas, and number of slices per pizza. Ensures that the number of slices per 
person comes out even. Displays the number of pieces each person should get, 
plus any remainder.

Challenge: Ensure that inputs are entered as numeric values greater than 0. 
Handle pluralization (piece vs. pieces)."""

import inflect

p = inflect.engine()

class Item():
    """People, pizzas, or pieces, with print method."""
    def __init__(self, name: str, val: int = 0): 
        self.name = name
        self.val = val
        self.unit = p.plural(self.name, self.val)

    def __repr__(self): 
        return f'{self.val} {self.unit}'

class Event():
    """The entire event, composed of people, pizzas, and pieces items."""
    def __init__(self, people: int, pizzas: int, pieces: int): 
        self.people = Item('person', people)
        self.pizzas = Item('pizza', pizzas)
        self.pieces = Item('piece', pieces)
        self._per_person = (self.pizzas.val * self.pieces.val) // self.people.val
        self.per_person = Item('piece', self._per_person)
        self._remainder = (self.pizzas.val * self.pieces.val) % self.people.val
        self.remainder = Item('piece', self._remainder)

    def __repr__(self): 
        return f'{self.people} with {self.pizzas}, {self.pieces} per pizza.\n' + \
            f'Each person gets {self.per_person} of pizza.\n' + \
                f'There {p.plural_verb("is", self.remainder.val)} {self.remainder} left over.'

if __name__ == "__main__": 

    while True: 

        print("How many people?")
        people: str = input()
        print("How many pizzas do you have?")
        pizzas: str = input()
        print("How many slices per pizza?")
        pieces: str = input()

        try: 
            inputs = [int(item) for item in [people, pizzas, pieces]]
            if any(item <= 0 for item in inputs):
                print("Please enter a number greater than 0")
                continue 
            else: 
                event = Event(inputs[0], inputs[1], inputs[2])
                print(event)
                break
        except(ValueError): 
            print("Enter it as a number, don't frikkin spell it out!")

        