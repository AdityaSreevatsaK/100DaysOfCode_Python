import warnings

from treasure_island_art import treasure_island_logo

warnings.filterwarnings("ignore", category=SyntaxWarning)

print("Day 3 - 100 Days of Code.")
print("Welcome to Treasure Island.")
print(treasure_island_logo)
print("Your mission is to find the treasure.")
crossroad = input("You're at a cross road. Where do you want to do? Type 'left' or 'right'. \n")
if crossroad.lower() == "left":
    lake = input("You've come to a lake. There is an island in the middle of the lake. "
                 "Type 'wait' to wait for a boat. Type 'swim' to swim across. \n")
    if lake.lower() == "wait":
        island = input("You arrive at the island unharmed. There is a house with 3 doors. "
                       "One red, one yellow and one blue. Which colour do you choose? \n").lower()
        if island == "red":
            print("It's a room full of fire. Game Over!")
        elif island == "yellow":
            print("You found the treasure! You Win!!")
        elif island == "blue":
            print("You enter a room of beasts. Game Over!")
        else:
            print("You chose a door that doesn't exist. Game Over!")
    else:
        print("You get attacked by an angry trout. Game Over!")
else:
    print("You fell into a hole. Game Over.")
