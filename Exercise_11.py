"""Program to convert euros to US dollars. 

Constraints: Ensure that fractions of a cent are rounded up to
the next penny. 

Challenges: 
* Build a dictionary of conversion rates and prompt 
for the countries instead of the rates. 
* Get exchange rates from an API
* My addition: Use command line arguments instead of prompts."""

import sys

# TO DO: Set up API https://openexchangerates.org/

if __name__ == '__main__':
    
    try: 
        currency = sys.argv[1]
        amount = sys.argv[2]
        print((currency, amount))
    except(IndexError):
        print("Please enter the currency and the amount")
    
