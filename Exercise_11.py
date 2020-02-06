"""Program to convert euros to US dollars. 

Constraints: Ensure that fractions of a cent are rounded up to
the next penny. 

Challenges: 
* Build a dictionary of conversion rates and prompt 
for the countries instead of the rates. 
* Get exchange rates from an API
* My addition: Use command line arguments instead of prompts."""

import os
import requests
import sys

API_BASE = 'https://openexchangerates.org/api/'
APP_ID = os.environ['APP_ID']
endpoint = os.path.join(API_BASE, ('latest.json?app_id=' + APP_ID))

# Wrap this in try except
response = requests.get(endpoint)

try: 
    currency = sys.argv[1]
    amount = sys.argv[2]
    output = (currency, amount)
except(IndexError):
    output = "Please enter the currency and the amount"

if __name__ == '__main__':
    # Temporary test
    print(response.json())
    
