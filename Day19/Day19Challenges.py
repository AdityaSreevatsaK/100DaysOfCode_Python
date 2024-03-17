from turtle import Screen, Turtle

turtle = Turtle()
screen = Screen()
zero = 0
ten = 10


def penup_home_pendown():
    turtle.penup()
    turtle.goto(zero, zero)
    turtle.pendown()


def turtle_moves_forward():
    turtle.forward(ten)


def turtle_moves_backwards():
    turtle.right(180)
    turtle_moves_forward()


def clear_screen():
    screen.clear()
    penup_home_pendown()


def counter_clockwise():
    turtle.setheading(turtle.heading() + ten)


def clockwise():
    turtle.setheading(turtle.heading() - ten)


def etch_a_sketch():
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
