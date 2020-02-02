"""Program to determine how many years you have left until
retirement and the year you can retire.

Constraints: Don't hard code the current year, use system time.

Challenge: Handle situations where the program returns a negative 
number by stating that the user can already retire."""

import datetime

current_year: int = datetime.datetime.now().year

if __name__ == "__main__": 

    print("What is your current age?")
    age_current: int = int(input())
    print("At what age would you like to retire?")
    age_retire: int = int(input())

    years_left: int = age_retire - age_current

    if years_left <= 0:
        print("You're already that age, so just retire!")
    else: 
        print(f'You have {years_left} years left until you can retire.')
        print(f'It\'s {current_year}, so you can retire in {current_year + years_left}.')