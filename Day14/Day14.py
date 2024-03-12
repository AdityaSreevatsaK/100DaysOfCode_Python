import random
import warnings

import follower_count_art
from follower_count_data import data

with warnings.catch_warnings():
    warnings.simplefilter('ignore', SyntaxWarning)
    warnings.warn('bad', SyntaxWarning)
print("Day 14 - 100 Days of Code.")
print("Welcome to 'Who has more followers?'")
print(follower_count_art.follower_count_logo)

is_user_choice_correct = True
zero = 0
one = 1
user_score = zero


def get_random_group():
    """
    Description:
        Method to get a random group from the local data.
    Return:
        dict: Dictionary of group data.
    """
    return random.choice(data)


while is_user_choice_correct:
    print("Group 1:")
    groupA = get_random_group()
    print(f"{groupA['name']}, a {groupA['description']}, from {groupA['country']}")
    print(follower_count_art.groupAVersusGroupB)
    print("Group 2:")
    groupB = groupA
    while groupB == groupA:
        groupB = get_random_group()
    print(f"{groupB['name']}, a {groupB['description']}, from {groupB['country']}")
    user_guess = int(input("Guess who has more followers. Group '1' or Group '2'?\n"))
    if ((groupA["follower_count"] > groupB["follower_count"] and user_guess == one)
            or (groupA["follower_count"] < groupB["follower_count"] and user_guess == 2)):
        print("That is correct! ;)")
        user_score += one
    else:
        is_user_choice_correct = False
        print("That is incorrect. :(\nGame Over.")
    print("Your score:", user_score)
