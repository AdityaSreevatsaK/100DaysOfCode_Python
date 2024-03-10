import random
import warnings

from number_guesser_art import number_guesser_logo

with warnings.catch_warnings():
    warnings.simplefilter('ignore', SyntaxWarning)
    warnings.warn('bad', SyntaxWarning)

print("Day 12 - 100 Days of Code.")
print("Welcome to the Number Guesser.")
print(number_guesser_logo)

zero = 0
one = 1
turns_remaining = 5 if input(
    "Would you like to play the game at 'easy' or 'hard' difficulty?\n").lower() == "hard" else 10


def get_random_number():
    """
    Description:
        Method to get a random number between 1 and 100.
    Return:
        int: An integer between 1 and 100.
    """
    return random.randint(one, 101)


random_number = get_random_number()
while turns_remaining > zero:
    guess = int(input("Guess a number: "))
    if guess - one == random_number:
        print("Very close. Guess higher.")
    elif guess + one == random_number:
        print("Very close. Guess lower.")
    elif guess > random_number:
        print("Guess lower!")
    elif guess < random_number:
        print("Guess higher!")
    else:
        print("Correct guess! Congrats! :)")
        break
    turns_remaining -= one
    if turns_remaining == zero:
        print("Oh no. You failed to guess the number. It was", random_number)
