"""Mad lib program that prompts for a noun, verb, an adverb, and an 
adjective, and injects them into a simple story.  

Constraints: Use a single output statement to produce this output. If your 
language supports string interpolation or string substitution, use it for 
this exercise."""

print("Enter a noun:")
noun: str = input()
print("Enter a verb:")
verb: str = input()
print("Enter an adjective:")
adjective: str = input()
print("Enter an adverb:")
adverb: str = input()

output: str = f'Do you {verb} your {adjective} {noun} {adverb}? \
That\'s a good story.'

print(output)