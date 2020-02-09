"""Program to perform currency conversions. WORK IN PROGRESS

Constraints: Ensure that fractions of a cent are rounded up to
the next penny. 

My innovations: 
* Use command line arguments instead of prompts
* Allow conversion between any currencies: 
*    $ python Exercise_11.py 10 USD EUR converts 10 USD to EUR

Challenges: 
* Build a dictionary of conversion rates and prompt 
for the countries instead of the rates. 
* Get exchange rates from an API."""

import json
import os
import requests
import sys
from dotenv import load_dotenv
from typing import Tuple

load_dotenv() # Contains APP_ID as environment variable from .env file
API_BASE: str = 'https://openexchangerates.org/api/'
APP_ID: str = os.environ['APP_ID']
endpoint: str = os.path.join(API_BASE, ('latest.json?app_id=' + APP_ID))

try: 
    input_currency: str = sys.argv[1]
    input_amount: float = float(sys.argv[2])
except(IndexError):
    output = "Please enter the currency and the amount"

# TO DO: Make a class

def get_rates(endpoint: str, currency: str) -> float:
    response = requests.get(endpoint)
    parsed = response.json() 
    return parsed['rates'][currency]

def convert_amount(rate: float, amount: float) -> float:
    return amount / rate

# TO DO: Wrap this in try except

if __name__ == '__main__':
    rate = get_rates(endpoint, input_currency)
    out_amount = convert_amount(rate, input_amount)

    output = f'{str(input_amount)} units of currency {input_currency} = \
{str(out_amount)} USD'

    print(output)
    
