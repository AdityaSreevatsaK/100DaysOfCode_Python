import os
import time
from turtle import Screen, Turtle

from PIL import Image

from Cars import Cars
from Player import Player
from Scoreboard import Scoreboard

zero = 0
game_over = False

turtle_helper = Turtle()
turtle_helper.penup()
turtle_helper.hideturtle()
turtle_helper.speed("fastest")
screen = Screen()
screen.tracer(zero)
screen.setup(width=600, height=600)
player = Player()
scoreboard = Scoreboard()
scoreboard.update_level()
cars = Cars()
turtle_helper.penup()
turtle_helper.goto(100, 275)
turtle_helper.pencolor("violetred")
turtle_helper.write("Day 23 - Turtle Crossing", align="right", font=("Palatino Linotype", 15, "italic"))
turtle_helper.pendown()


def display_game_over():
    """
    Description:
        Method to display that the game is over.
    """
    turtle_helper.penup()
    turtle_helper.goto(-100, zero)
    turtle_helper.pencolor("brown2")
    turtle_helper.write("GAME OVER!", font=("Courier", 25, "bold"))


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


while not game_over:
    screen.update()
    time.sleep(0.1)
    screen.listen()
    screen.onkey(player.move_turtle, key="Up")
    cars.generate_random_car()
    cars.move_cars()

    for car in cars.car_list:  # To check collision between player and cars.
        if player.distance(car) < 25:
            game_over = True
            display_game_over()

    if player.ycor() >= 280:  # Indicating level completion.
        scoreboard.clear()
        scoreboard.update_level()
        player.hideturtle()
        player = Player()
        cars.level_up()

fileName = "Turtle Crossing"
turtle_helper.getscreen().getcanvas().postscript(file=fileName + '.eps')
img = Image.open(fileName + '.eps')
img.save(fileName + '.jpg')
img.close()
delete_file(r"Turtle Crossing.eps")

screen.exitonclick()
