from Exercise_7 import Room

def test_room():
    room = Room(3, 4)
    room.find_area()
    assert room.length == 3, "Incorrectly records length"
    assert room.width == 4, "Incorrectly records width" 
    assert room.area_feet == 12, "Incorrectly calculates area in feet"
    assert room.area_meters == 1.1148364800000001, "Incorrectly calculates area in meters"

if __name__ == "__main__":
    test_room()