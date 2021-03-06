"""Program that prompts for an input string and displays output that
shows the input string and the  number of characters the string contains.

Constraint: Use a single output statement to construct the output. Use 
a built-in function to determine the length of the string.

Challenge: If the user enters nothing, state that the user must enter
something into the program."""

print("What is the input string?")

while True: 
    string: str = input()
    if len(string) == 0: 
        print("You didn't enter anything. Please enter a string.")
    else: 
        output: str = f'{string} has {str(len(string))} characters.'
        print(output)
        break