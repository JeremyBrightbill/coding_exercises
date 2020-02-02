"""Description"""

CONVERSION = 0.09290304

class Room(): 

    def __init__(self): 
        self.length: float = 0
        self.width: float = 0

    def find_area(self):
        self.area_feet: float = self.length * self.width
        self.area_meters: float = self.area_feet * CONVERSION

    def print_output(self):
        output = f"""You entered dimensions of {self.length} feet by {self.width} feet.
The area is:
{self.area_feet} square feet
{self.area_meters} square meters"""
        print(output)

if __name__ == "__main__":

    room = Room()
    print("What is the length of the room in feet?")
    room.length = float(input())
    print("What is the width of the room in feet?")
    room.width = float(input())
    room.find_area()
    room.print_output()