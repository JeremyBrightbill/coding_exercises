"""Program to perform currency conversions. WORK IN PROGRESS

Constraints: Ensure that fractions of a cent are rounded up to
the next penny. 

My innovations: 
* Get exchange rates from Open Exchange API
* Use command line arguments instead of prompts
* Allow conversion between any currencies with the following input: 
     $ python Exercise_11.py 10 USD EUR converts 10 USD to EUR
* Validate inputs using argparse
"""

import argparse
import math
import os
import requests
import sys
from dotenv import load_dotenv

load_dotenv() # Contains APP_ID as environment variable from .env file
API_BASE: str = 'https://openexchangerates.org/api/'
APP_ID: str = os.environ['APP_ID']

# TO DO: Move these utility functions to a package

def to_usd(amount: float, rate: float) -> float: 
    return amount / rate

def from_usd(amount: float, rate: float) -> float: 
    return amount * rate

def round_up(n: float, decimals: int) -> float:
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

class Converter(): 

    def __init__(self) -> None:
        self.rates: dict = self.get_rates_all()

    def get_rates_all(self) -> dict:
        endpoint: str = f'{API_BASE}latest.json?app_id={APP_ID}'
        response = requests.get(endpoint)
        return response.json()['rates']

    # TO DO: Error should return list of available currencies
    
    def validate_input(self) -> None: 
        parser = argparse.ArgumentParser()
        parser.add_argument("amount", help="amount", type=float)
        parser.add_argument("currency_from", help="currency to convert from", type=str)
        parser.add_argument("currency_to", help="currency to convert to", type=str)
        args = parser.parse_args()
        if (args.currency_from not in self.rates) or (args.currency_to not in self.rates): 
            raise ValueError("Invalid currency")
        inputs = vars(args)
        self.amount, self.currency_from, self.currency_to = inputs.values()

    def convert_currency(self) -> float: 
        if self.currency_from == 'USD': 
            rate = self.rates[self.currency_to]
            self.output = from_usd(self.amount, rate)
        if self.currency_to == 'USD': 
            rate = self.rates[self.currency_from]
            self.output = to_usd(self.amount, rate)
        else: 
            rate1, rate2 = self.rates[self.currency_from], self.rates[self.currency_to]
            amount_usd = to_usd(self.amount, rate1)
            self.output = from_usd(amount_usd, rate2)
        return format(round_up(self.output, 2), '.2f')

if __name__ == '__main__':
    
    converter = Converter()
    converter.validate_input()
    output = converter.convert_currency()

    print(output)
    
