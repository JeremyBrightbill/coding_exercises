"""Write a program that prompts for two numbers. Print the sum, 
difference, product, and quotient of those numbers.

Constraint: Keep the inputs and outputs separate from the numerical
conversions and other processing.

Challenge: Revise the program to accept only positive numeric values. 
Break the program into functions."""

def calculate(num1: float, num2: float) -> float:
    output = (num1 + num2, num1 - num2, \
        num1 * num2, num1 / num2)
    return output

while True:

    print("Enter the first number:")
    num1: str = input()
    print("Enter the second number:")
    num2: str = input()

    try: 
        if float(num1) <= 0 or float(num2) <= 0:
            print("Please enter a number greater than 0")
            continue
        else: 
            results = calculate(float(num1), float(num2))
            for operation, result in zip(['+', '-', '*', '/'], results):
                print(f'{num1} {operation} {num2} = {result}')
            break
    except(ValueError): 
        print("Enter it as a number, don't frikkin spell it out!")
    