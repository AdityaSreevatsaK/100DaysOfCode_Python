from functools import reduce

from silent_auction_art import silent_auction_logo

print("Day 9 - 100 Days of Code.")
print("Welcome to the Silent Auction.")
print(silent_auction_logo)

users_and_bids = {}
is_more_bidders = True


def get_auction_winner():
    """
    Description:
        Method to determine the highest bidder in the auction.
    Returns:
        str:    The name of the highest bidder.
        float:  The highest bid.
    """
    highest_bid = reduce(lambda bid1, bid2: bid1 if bid1 > bid2 else bid2, users_and_bids.values())
    highest_bidder = None
    for key, value in users_and_bids.items():
        if value == highest_bid:
            highest_bidder = key
    return highest_bidder, highest_bid


while is_more_bidders:
    name_of_bidder = input("Enter your name:\n")
    bid_amount = float(input("Enter your bid amount in Rupees:\n"))
    users_and_bids[name_of_bidder] = bid_amount
    is_more_bidders = True if input("Are there any more bidders (yes/no)?\n").lower() == "yes" else False

winner, winning_bid = get_auction_winner()
print(f"The winner of the auction is {winner} with a bid of Rs. {winning_bid}")
