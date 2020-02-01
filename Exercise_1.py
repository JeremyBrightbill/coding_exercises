"""Program that prompts user for their name, then replies with the name 
in a greeting.

Constraint: Keep the input, string concatenation, and output separate"""

print("What is your name?")
name: str = input()
greeting: str = "Hello, " + name + ", nice to meet you!"
print(greeting)