""" AUTHOR  - PRINCE SHARMA
    DATE    - 28/4/2024 7:24 PM
    WORKING - Guessing Game
"""

import random

attempts = 0
secret_number = random.randint(1,100)

print("Welcome to the Guessing Game!")
print("I've selected a number between 1 and 100. Try to guess it!")

while True :
    try :
        guess = int(input("Enter your guess (1-100) - "))
        attempts += 1
        
        if guess < secret_number :
            print("Too low! Try again.")
        elif guess > secret_number :
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it right in {attempts} attempts!")
            break
    except :
        print("Invalid Input")