from turtle import Screen, Turtle

turtle = Turtle()
screen = Screen()
zero = 0
ten = 10

print("Day 19 - 100 Days of Code.")
print("Welcome to Etch-A-Sketch.")


def penup_home_pendown():
    """
    Description:
        Method to move the turtle to origin.
    """
    turtle.penup()
    turtle.goto(zero, zero)
    turtle.pendown()


def turtle_moves_forward():
    """
    Description:
        Method to move turtle forward.
    """
    turtle.forward(ten)


def turtle_moves_backwards():
    """
    Description:
        Method to move turtle backward.
    """
    turtle.right(180)
    turtle_moves_forward()


def clear_screen():
    """
    Description:
        Method to clear screen.
    """
    screen.clear()
    penup_home_pendown()


def counter_clockwise():
    """
    Description:
        Method to set direction as current angle + 10.
    """
    turtle.setheading(turtle.heading() + ten)


def clockwise():
    """
    Description:
        Method to set direction as current angle - 10.
    """
    turtle.setheading(turtle.heading() - ten)


def etch_a_sketch():
    """
    Description:
        Method for etch a sketch game.
    """
    turtle.penup()
    turtle.goto(-250, 250)
    turtle.pendown()
    turtle.write("Etch-A-Sketch!", font=('Arial', 20, 'bold'), )
    penup_home_pendown()
    screen.onkey(turtle_moves_forward, "w")
    screen.onkey(turtle_moves_backwards, "s")
    screen.onkey(counter_clockwise, "a")
    screen.onkey(clockwise, "d")
    screen.onkey(clear_screen, "c")


screen.listen()
etch_a_sketch()
