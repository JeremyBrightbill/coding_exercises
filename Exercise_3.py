"""Program that asks for a quote and an author, then displays the
quote in quotation marks and the author. 

Constraints: Use a single output statement to produce this output, 
using appropriate string-escaping techniques for quotes. If your language
supports string interpolation or string substitution, don't use it for
this exercise. Use string concatenation instead."""

print("What is the quote? (Enter without quotation marks.)")
quote: str = input()
print("Who said it?")
author: str = input()

output: str = f'{author} says, \"{quote}"'
print(output)