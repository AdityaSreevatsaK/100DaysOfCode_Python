import os
import random

from PIL import Image

zero = 0
hundred = 100
two_hundred_and_fifty = 250
jpg_extension = ".jpg"
eps_extension = ".eps"
color_list = ["green", "blue", "black", "red", "aquamarine", "darkolivegreen"]


def write_heading_for_screen(turtle, text, coordinates):
    """
    Description:
        Method to write headings for the various screens.
    """
    turtle.penup()
    turtle.goto(coordinates)
    turtle.pendown()
    turtle.write(text, move=False, align='left', font=('Arial', 20, 'bold'))
    turtle.penup()
    turtle.goto(zero, zero)
    turtle.pendown()


def perform_challenges(turtle):
    turtle.speed("fastest")
    turtle.hideturtle()

    write_heading_for_screen(turtle, "Challenge 1 - Draw a square", (-150, 150))
    for _ in range(4):
        turtle.forward(hundred)
        turtle.right(90)

    challenge1 = "Challenge1"
    turtle.getscreen().getcanvas().postscript(file=challenge1 + eps_extension)
    img = Image.open(challenge1 + eps_extension)
    img.save(challenge1 + jpg_extension)
    img.close()
    challenge1_eps_file = r"Challenge1.eps"
    delete_eps_files(challenge1_eps_file)
    turtle.clear()

    write_heading_for_screen(turtle, "Challenge 2 - Draw a dashed line.", (-150, 150))
    for iterator in range(10):
        if iterator % 2 == zero:
            turtle.penup()
        turtle.forward(10)
        turtle.pendown()

    challenge2 = "Challenge2"
    turtle.getscreen().getcanvas().postscript(file=challenge2 + eps_extension)
    img = Image.open(challenge2 + eps_extension)
    img.save(challenge2 + jpg_extension)
    img.close()
    challenge2_eps_file = r"Challenge2.eps"
    delete_eps_files(challenge2_eps_file)
    turtle.clear()

    write_heading_for_screen(turtle, "Challenge 3 - Draw shapes - Triangle - Decagon.", (-250, 150))
    for shape_sides in range(3, 11):
        turtle.color(random.choice(color_list))
        angle_of_shape = 360 / shape_sides
        for _ in range(shape_sides):
            turtle.forward(hundred)
            turtle.right(angle_of_shape)

    challenge3 = "Challenge3"
    turtle.getscreen().getcanvas().postscript(file=challenge3 + eps_extension)
    img = Image.open(challenge3 + eps_extension)
    img.save(challenge3 + jpg_extension)
    img.close()
    challenge3_eps_file = r"Challenge3.eps"
    delete_eps_files(challenge3_eps_file)
    turtle.clear()

    write_heading_for_screen(turtle, "Challenge 4 - Spirograph.", (-150, 250))
    turtle.goto(zero, zero)

    for angle in range(72):
        turtle.color(random.choice(color_list))
        turtle.circle(hundred)
        turtle.right(5)

    challenge4 = "Challenge4"
    turtle.getscreen().getcanvas().postscript(file=challenge4 + eps_extension)
    img = Image.open(challenge4 + eps_extension)
    img.save(challenge4 + jpg_extension)
    img.close()
    challenge4_eps_file = r"Challenge4.eps"
    delete_eps_files(challenge4_eps_file)
    turtle.clear()


def delete_eps_files(file_path):
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("You don't have permission to delete this file")
