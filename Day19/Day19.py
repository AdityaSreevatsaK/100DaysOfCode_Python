import os
import random
from functools import reduce
from turtle import Screen, Turtle

from PIL import Image

print("Day 19 - 100 Days of Code.")
print("Welcome to Turtle Race.")

turtle = Turtle()
screen = Screen()
screen.setup(width=500, height=700)
zero = 0
ten = 10
twenty = 20
fifty = 50
one_hundred_and_eighty = 180
two_hundred_and_fifty = 250
race_not_completed = True
underscore_string = "_"
turtle_string = "turtle"
fastest_string = "fastest"
user_bet = ""
turtle_object_list = []
race_turtle_distance = [zero] * 7

turtle_list = ["Violet", "Indigo", "Blue", "Green", "Yellow", "Orange", "Red"]
turtle_color_list = ["dark slate blue", "blue", "deep sky blue", "lime", "gold", "dark orange", "red"]

while user_bet.title() not in turtle_list:
    user_bet = screen.textinput(title="Choose your turtle!",
                                prompt=f"Which turtle will win? Enter a colour from {turtle_list}.")


def draw_start_and_finish_lines(x_coordinate):
    """
    Description:
        Method to draw the start and end lines for the race.
    """
    turtle.penup()
    turtle.goto(x_coordinate, 100)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(400)
    turtle.right(-90)


def turtle_moves_forward(distance=ten):
    """
    Description:
        Method which causes the turtle to move forward by a distance of given argument.
    """
    turtle.forward(distance)


def move_random_distance(coloured_turtle):
    """
    Description:
        Method to move the turtle by a random distance between 10 and 50.
    """
    random_distance = random.randint(ten, twenty)
    coloured_turtle.forward(random_distance)
    return random_distance


def declare_and_initialise_turtles():
    """
    Description:
        Method to declare the turtles and set their speed and colour. Also, to move them to required positions.
    """
    for iterator in range(len(turtle_list)):
        coloured_turtle = Turtle(shape=turtle_string)
        coloured_turtle.penup()
        coloured_turtle.speed(fastest_string)
        coloured_turtle.goto(-one_hundred_and_eighty, fifty - (iterator * fifty))
        coloured_turtle.color(turtle_color_list[iterator])
        turtle_object_list.append(coloured_turtle)


def racing_turtles():
    """
    Description:
        Method to proceed with the race. Also alters the distance travelled by turtle as required.
    """
    for race_turtle in turtle_object_list:
        race_turtle_distance[turtle_object_list.index(race_turtle)] += move_random_distance(race_turtle)
        if race_turtle_distance[turtle_object_list.index(race_turtle)] >= 360:
            global race_not_completed
            race_not_completed = False


def get_winner():
    """
    Description:
        Method to get the winner of the race.
    Return:
        Returns the name of the turtle who won the race.
    """
    return turtle_list[  # Finding the turtle which has travelled the greatest distance.
        race_turtle_distance.index(  # Finding the index of the greatest distance.
            reduce(lambda d1, d2: d1 if d1 > d2 else d2, race_turtle_distance)  # Finding the greatest distance.
        )
    ]


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


turtle.hideturtle()
turtle.speed(fastest_string)
turtle.penup()
turtle.goto(-100, 200)
turtle.pendown()
turtle.write("Turtle Race!!", font=("Arial", twenty, "bold"))
draw_start_and_finish_lines(-one_hundred_and_eighty)
draw_start_and_finish_lines(one_hundred_and_eighty)
declare_and_initialise_turtles()
while race_not_completed:
    racing_turtles()
winner = get_winner()
if user_bet == winner:
    print("Yay! You have won the bet. 😁")
else:
    print("Oh no! You lost the bet. 😢")
print(winner, "won the race!")

fileName = "Turtle Race"
turtle.getscreen().getcanvas().postscript(file=fileName + '.eps')
img = Image.open(fileName + '.eps')
img.save(fileName + '.jpg')
img.close()
delete_file(r"Turtle Race.eps")
screen.exitonclick()
