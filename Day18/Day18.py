import random
from turtle import Screen, Turtle, colormode

import colorgram
from PIL import Image

import Day18Challenges

print("Day 18 - 100 Days of Code.")
print("Welcome to Hirst Painting!")

turtle = Turtle()
screen = Screen()
screen.setup(width=1.0, height=1.0)
challenge = Day18Challenges
challenge.perform_challenges(turtle)

zero = 0
ten = 10
fifty = 50
hundred = 100
endpoint_colour = 255
threshold_rgb = 230

challenge.write_heading_for_screen(turtle, "Damien Hirst Spot Painting By Python", (-250, 300))
turtle.hideturtle()
turtle.penup()
turtle.setheading(225)
turtle.setheading(220)
turtle.forward(300)
turtle.setheading(zero)
turtle.pendown()
starting_point = turtle.pos()

colormode(endpoint_colour)

turtle.shape("turtle")
colour_list = []
for color in colorgram.extract("Hirst Spot Painting.jpg", fifty):
    red, green, blue = color.rgb.r, color.rgb.g, color.rgb.b
    if red < threshold_rgb and green < threshold_rgb and blue < threshold_rgb:
        colour_list.append((red, green, blue))

turtle.speed("fastest")
turtle.pensize(20)


def get_random_color():
    """
    Description:
        Method to get a random RGB colour.
    Return:
        Returns an RGB tuple.
    """
    rgb_value = (random.randint(zero, endpoint_colour),
                 random.randint(zero, endpoint_colour),
                 random.randint(zero, endpoint_colour))
    return rgb_value


for x_axis in range(ten):
    for _ in range(ten):
        turtle.color(random.choice(colour_list))
        turtle.pendown()
        turtle.dot()
        turtle.penup()
        turtle.forward(fifty)
        turtle.pendown()
    turtle.penup()
    turtle.goto(starting_point[zero], turtle.pos()[1] + fifty)

fileName = "Damien Hirst Spot Painting By Python"
turtle.getscreen().getcanvas().postscript(file=fileName + '.eps')
img = Image.open(fileName + '.eps')
img.save(fileName + '.jpg')
img.close()
damien_hirst_spot_painting = r"Damien Hirst Spot Painting By Python.eps"
challenge.delete_eps_files(damien_hirst_spot_painting)
screen.bye()
