"""Program to convert euros to US dollars. 

Constraints: Ensure that fractions of a cent are rounded up to
the next penny. 

Challenges: 
* Build a dictionary of conversion rates and prompt 
for the countries instead of the rates. 
* Get exchange rates from an API
* My addition: Use command line arguments instead of prompts."""

import sys

API_BASE = https://openexchangerates.org/api/
# TO DO: Set APP_ID as environment variable 

try: 
    currency = sys.argv[1]
    amount = sys.argv[2]
    output = (currency, amount)
except(IndexError):
    output = "Please enter the currency and the amount"

if __name__ == '__main__':
    
    print(output)
    
