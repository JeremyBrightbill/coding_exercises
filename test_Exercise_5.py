from Exercise_5 import calculate

def test_calculate(): 
    assert calculate(4, 2) == (6, 2, 8, 2), "Something is wrong"
    assert calculate(2, 4) == (6, -2, 8, 0.5), "Doesn't work if second number is larger"

if __name__ == "__main__":
    test_calculate()