import os
from turtle import Screen, Turtle

import pandas as pd
from PIL import Image

print("Day 25 - 100 Days of Code.")
print("Welcome to India States Game.")
xyCor = open("IndianStatesXYCor.csv", mode="a")
zero = 0
user_score = zero
scoreboard = Turtle()
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.goto(50, 300)
max_score = 36
graphics_turtle = Turtle()
graphics_turtle.hideturtle()
graphics_turtle.penup()
graphics_turtle.speed("fastest")
graphics_turtle.pencolor("purple")
screen = Screen()
screen.setup(width=700, height=700)
screen.title("India States Game!")
screen.bgpic("India Map.gif")
user_guess = ""
correct_guesses = []
states_data = pd.read_csv("IndianStatesXYCor.csv")
exit_trigger = False


def game_won():
    """
    Description:
        Method to display that the game is won after user has named all the states.
    """
    graphics_turtle.goto(100, 230)
    graphics_turtle.pencolor("limegreen")
    graphics_turtle.write("YOU WIN!", font=("Palatino Linotype", 25, "italic"))
    update_score()
    save_image()


def save_image():
    """
    Description:
        Method to save the image after game is complete.
    """
    file_name = "Indian States Game"
    graphics_turtle.getscreen().getcanvas().postscript(file=file_name + '.eps')
    img = Image.open(file_name + '.eps')
    img.save(file_name + '.jpg')
    img.close()
    delete_file(r"Indian States Game.eps")


def update_score():
    """
    Description:
        Method to keep track and update the score.
    """
    scoreboard.pencolor("orangered")
    scoreboard.clear()
    scoreboard.write(f"SCORE: {user_score}/{max_score}", font=("Courier", 20, "bold"))


def display_remaining_states():
    """
    Description:
        Method to display the remaining state names after user fails to do so.
    """
    for state in states_data.State.values:
        if state in correct_guesses:
            pass
        else:
            graphics_turtle.pencolor("darkslategray")
            display_state_name(state)


def exit_game():
    """
    Description:
        Method to exit the game.
    """
    update_score()
    display_remaining_states()
    save_image()
    return True


def delete_file(file_path):
    """
    Description:
        Method to delete the file at the given path.
    """
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("You don't have permission to delete this file")


def display_state_name(guess):
    """
    Description:
        Method to display the state name.
    """
    x_coordinate = float(states_data.xCoordinate[states_data.State == guess].iloc[zero])
    y_coordinate = float(states_data.yCoordinate[states_data.State == guess].iloc[zero])
    graphics_turtle.goto(x_coordinate, y_coordinate)
    graphics_turtle.write(guess, font=("Palatino Linotype", 10, "bold"))


update_score()

screen.listen()
screen.onkey(exit_game, key="Escape")
while user_score < max_score or exit_trigger:
    graphics_turtle.goto(123, 230)
    user_guess = screen.textinput(title="Know your country!", prompt="Name a state:")
    if user_guess is None:
        exit_trigger = exit_game()
        break
    user_guess = user_guess.title()
    if user_guess in states_data.State.values:
        if user_guess not in correct_guesses:
            display_state_name(user_guess)
            user_score += 1
            correct_guesses.append(user_guess)
            update_score()
        else:
            pass
    else:
        pass

if user_score == max_score:
    game_won()
screen.mainloop()
