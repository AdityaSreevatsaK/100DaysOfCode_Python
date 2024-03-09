print("Day 6 - 100 Days of Code.")
print("Welcome to the Reeborg's World.")
print("URL to Reeborg's World: https://reeborg.ca/reeborg.html")


def turn_left():
    print("Reeborg turns left.")


def right_is_clear():
    print("Function to check whether right side is clear.")


def front_is_clear():
    print("Function to check whether front side is clear.")


def at_goal():
    print("Function to check whether Reeborg has reached the goal.")


def move():
    print("Reeborg moves forward.")


while not at_goal():
    if right_is_clear():
        turn_left()
        turn_left()
        turn_left()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
