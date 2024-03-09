import sys
import warnings
import random

from blackjack_art import blackjack_logo

warnings.filterwarnings("ignore", category=SyntaxWarning)

print("Day 11 - 100 Days of Code.")
print("Welcome to the Blackjack Game.")
print(blackjack_logo)
one = 1
does_user_want_to_play = True
is_user_winner = False
is_dealer_winner = False
twenty_one = 21

def generate_random_card():
    """
    Description:
        Method to draw a random card.
    Return:
         Returns a random number from 2 to 12.
            2 to 10 - Regular Cards.
            11      - King.
            12      - Queen.
            13      - Jack.
            14      - Ace.
    """
    card_dealt = random.randint(2, 14)
    if card_dealt == 11:
        return "K"
    elif card_dealt == 12:
        return "Q"
    elif card_dealt == 13:
        return "J"
    elif card_dealt == 14:
        return "A"
    else:
        return card_dealt


def determine_total_and_alter_hand(dealt_hand: list):
    """
    Description:
        Method to determine the total for the hand dealt. Replacing K,Q and J with 10.
        A with 11 or 1 based on condition.
    Returns:
        list: New hand with correct values.
        int : Total of hand dealt.
    """
    dealt_hand_total = 0
    new_hand = []
    for index in range(len(dealt_hand)):
        if dealt_hand[index] in ["K", "Q", "J"]:
            dealt_hand_total += 10
            new_hand.append(10)
        elif dealt_hand[index] in range(2, 11):
            dealt_hand_total += dealt_hand[index]
            new_hand.append(dealt_hand[index])
        elif dealt_hand[index] == "A":
            if dealt_hand_total + 11 > twenty_one:
                dealt_hand_total += one
                new_hand.append(one)
            else:
                dealt_hand_total += 11
                new_hand.append(11)

    return new_hand, dealt_hand_total


def get_dealer_final_hand(dealers_initial_hand):
    """
    Description:
        Method to get the final hand for the dealer.
    Return:
        list: Final hand of the dealer.
    """
    dealers_initial_hand, dealers_initial_hand_total = determine_total_and_alter_hand(dealers_initial_hand)
    while dealers_initial_hand_total < 17:
        dealers_initial_hand.append(generate_random_card())
        dealers_initial_hand, dealers_initial_hand_total = determine_total_and_alter_hand(dealers_initial_hand)

    return dealers_initial_hand


def is_blackjack(users_hand, dealers_hand):
    """
    Description:
        Method to determine if either the user of the dealer have won the game with a blackjack.
    """
    users_hand, users_hand_total = determine_total_and_alter_hand(users_hand)
    dealers_hand, dealers_hand_total = determine_total_and_alter_hand(dealers_hand)
    print(f"Your cards: {user_hand}\nScore: {users_hand_total}")
    print(f"Dealer's first card: {dealers_hand[0]}\n")
    if users_hand_total > twenty_one:
        print("You lose. Hand grater than 21.")
        sys.exit()
    if users_hand_total == twenty_one and dealers_hand_total == twenty_one:
        print("You and the dealer have a score of 21. It is a draw.")
        sys.exit()
    if users_hand_total == twenty_one and dealers_hand_total != twenty_one:
        print("You have a score of 21. You win!! ;)")
        sys.exit()
    if users_hand_total != twenty_one and dealers_hand_total == twenty_one:
        print("Dealer has a score of 21. You lose. :(")
        sys.exit()


def determine_winner(users_hand, dealers_hand):
    """
    Description:
        Method to determine the winner if it's not a blackjack scenario.
    """
    users_hand, user_hand_total = determine_total_and_alter_hand(users_hand)
    dealers_hand, dealer_hand_total = determine_total_and_alter_hand(dealers_hand)
    if user_hand_total > dealer_hand_total:
        print("Your score is {user_hand_total} and the dealer's score is {dealer_hand_total}. You win! ;)")
        sys.exit()
    elif user_hand_total < dealer_hand_total:
        print("Your score is {user_hand_total} and the dealer's score is {dealer_hand_total}. You lose. :(")
        sys.exit()
    else:
        print("Your and the dealer have a score of {user_hand_total}. It's a draw.")
        sys.exit()


user_hand = [generate_random_card(), generate_random_card()]
dealer_hand = [generate_random_card(), generate_random_card()]

while does_user_want_to_play:
    does_user_want_to_play = True if (
            input("Do you want to play a game of blackjack (yes/no)?\n").lower() == "yes") else False
    if not does_user_want_to_play:
        print("Goodbye.")
        break
    is_blackjack(user_hand, dealer_hand)
    while not is_user_winner and not is_dealer_winner:
        hit_or_pass = True if input(
            "Enter 'yes' to get another card. Enter 'no' to pass.\n").lower() == "yes" else False
        if hit_or_pass:
            user_hand.append(generate_random_card())
        else:
            determine_winner(user_hand, dealer_hand)
        is_blackjack(user_hand, dealer_hand)
