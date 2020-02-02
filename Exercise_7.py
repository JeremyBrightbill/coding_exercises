"""Program that calculates the area of a room. Prompts for length and 
width of room in feet, then displays area in both square feet and 
square meters.

Constraint: Use a constant to hold the conversion factor.

TO DO: Refactor methods with @property"""

class Room(): 

    def __init__(self, length: float, width: float): 
        self.CONVERSION = 0.09290304
        self.length: float = length
        self.width: float = width

    def find_area(self):
        self.area_feet: float = self.length * self.width
        self.area_meters: float = self.area_feet * self.CONVERSION

    def print_output(self):
        output = f"""You entered dimensions of {self.length} feet by {self.width} feet.
The area is:
{self.area_feet} square feet
{self.area_meters} square meters"""
        print(output)

if __name__ == "__main__":

    print("What is the length of the room in feet?")
    length: str = input()
    print("What is the width of the room in feet?")
    width: str = input()
    room = Room(int(length), int(width))
    room.find_area()
    room.print_output()