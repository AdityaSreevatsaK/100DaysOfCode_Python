import random
import warnings

from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list

with warnings.catch_warnings():
    warnings.simplefilter('ignore', SyntaxWarning)
    warnings.warn('bad', SyntaxWarning)
print("Day 7 - 100 Days of Code.")
print("Welcome to Hangman.")
print(logo)

empty_string = ""
underscore = "_"
zero = 0
one = 1
lives_remaining = 7
word_guessed = False
random_word_list = list(word_list[random.randint(zero, 213)])
remaining_values = len(random_word_list)
status = underscore * remaining_values

for letter in random_word_list:
    print(underscore, end=empty_string)
print("\n")


def replace_unknown_with_user_entry(entry_from_user, current_status):
    """
    Description:
        Method to replace the underscores with the correctly guessed characters.
    Returns:
        str: The current status of the user's guess of the randomised word.
    """
    counter = zero
    current_status_list = list(current_status)
    for element in current_status_list:
        if element == underscore:
            if random_word_list[counter] == entry_from_user:
                current_status_list[counter] = entry_from_user
        else:
            current_status_list[counter] = element
        counter += one

    current_status = empty_string.join(current_status_list)
    print(current_status)
    return current_status


while lives_remaining > zero and word_guessed is False:
    user_entry = (input("Enter a character: "))
    if user_entry in random_word_list:
        print("Correct entry.")
        if user_entry not in status:
            remaining_values -= random_word_list.count(user_entry)
        status = replace_unknown_with_user_entry(user_entry, status)
        if remaining_values == zero:
            word_guessed = True
    else:
        print("Incorrect entry. :(\nLost a life.")
        print(stages[lives_remaining - one])
        lives_remaining -= one
        print(status)
    if lives_remaining == zero:
        print("Oh no! Game over.")
        print(f"The correct answer was {empty_string.join(random_word_list)}.")
        break
    if word_guessed is True:
        print("Yay! Word guessed correctly. You win!")
        break
