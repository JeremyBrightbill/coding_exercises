"""Write a program that prompts for two numbers. Print the sum, 
difference, product, and quotient of those numbers.

Constraint: Keep the inputs and outputs separate from the numerical
conversions and other processing.

Challenge: Revise the program to accept only positive numeric values."""

print("Enter the first number:")
num1: str = input()
print("Enter the second number:")
num2: str = input()

num_sum: int = int(num1) + int(num2)
num_diff: int = int(num1) - int(num2)
num_prod: int = int(num1) * int(num2)
num_quot: int = int(num1) / int(num2)

output: str = f"""
{str(num1)} + {str(num2)} = {str(num_sum)}
{str(num1)} - {str(num2)} = {str(num_diff)}
{str(num1)} * {str(num2)} = {str(num_prod)}
{str(num1)} / {str(num2)} = {str(num_quot)}
"""

print(output)