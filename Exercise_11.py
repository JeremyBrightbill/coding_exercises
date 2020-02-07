"""Program to convert any currency to US dollars. IN PROGRESS

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
from dotenv import load_dotenv
from typing import Tuple

load_dotenv() # Contains APP_ID as environment variable from .env file
API_BASE: str = 'https://openexchangerates.org/api/'
APP_ID: str = os.environ['APP_ID']
endpoint: str = os.path.join(API_BASE, ('latest.json?app_id=' + APP_ID))

# TO DO: Wrap this in try except
response = requests.get(endpoint)

try: 
    currency: str = sys.argv[1]
    amount:str = sys.argv[2]
    output = (currency, amount)
except(IndexError):
    output = "Please enter the currency and the amount"

if __name__ == '__main__':
    # Temporary test
    print(response.json())
    # TO DO: Set up the rest of functionality
