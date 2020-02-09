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

import argparse, os, requests, sys
from dotenv import load_dotenv
from typing import Tuple # And others

load_dotenv() # Contains APP_ID as environment variable from .env file
API_BASE: str = 'https://openexchangerates.org/api/'
APP_ID: str = os.environ['APP_ID']

# TO DO: Make a class

def get_rates_all() -> dict:
    endpoint: str = f'{API_BASE}latest.json?app_id={APP_ID}'
    response = requests.get(endpoint)
    return response.json()['rates']

# def get_rate(currency: str, rates: dict) -> float: 
#     return rates[currency]

def to_usd(amount: float, rate: float) -> float: 
    return amount / rate

def from_usd(amount: float, rate: float) -> float: 
    return amount * rate

def validate_input(rates: dict) -> dict: 
    parser = argparse.ArgumentParser()
    parser.add_argument("amount", help="amount", type=float)
    parser.add_argument("currency_from", help="currency to convert from", type=str)
    parser.add_argument("currency_to", help="currency to convert to", type=str)
    args = parser.parse_args()
    if (args.currency_from not in rates) or (args.currency_to not in rates): 
        raise ValueError("Invalid currency")
    return vars(args)

def do_conversion(amount: float, currency1: str, currency2: str, rates: dict) -> float: 
    if currency1 == 'USD': 
        rate = rates[currency2]
        return from_usd(amount, rate)
    if currency2 == 'USD': 
        rate = rates[currency1]
        return to_usd(amount, rate)
    else: 
        rate1, rate2 = rates[currency1], rates[currency2]
        amount_usd = to_usd(amount, rate1)
        amount_out = from_usd(amount_usd, rate2)
        return amount_out

# TO DO: Wrap this in try except

if __name__ == '__main__':
    
    rates = get_rates_all()
    inputs = validate_input(rates)
    amount, currency_from, currency_to = inputs.values()
    

#     output = f'{str(input_amount)} units of currency {input_currency} = \
# {str(out_amount)} USD'

    #output = problematic

    print([amount, currency_from, currency_to])
    
