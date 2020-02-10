# Utility functions for use in the other programs

import math

def calculate_all(num1: float, num2: float) -> float:
    output = (num1 + num2, num1 - num2, \
        num1 * num2, num1 / num2)
    return output

def to_usd(amount: float, rate: float) -> float: 
    return amount / rate

def from_usd(amount: float, rate: float) -> float: 
    return amount * rate

def round_up(n: float, decimals: int) -> float:
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier