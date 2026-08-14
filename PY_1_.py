# Number Guessing Game
# This project uses loops, conditions, and random numbers — a great starter.


import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    number_to_guess = random.randint(1, 100)  # computer picks a number
    attempts = 0

    while True:
        guess = int(input("Enter your guess (1-100): "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"🎉 Correct! The number was {number_to_guess}.")
            print(f"You guessed it in {attempts} attempts.")
            break

number_guessing_game()