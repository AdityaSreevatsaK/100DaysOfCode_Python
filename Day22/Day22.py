import time
from turtle import Screen, Turtle

import Ball
import Paddle
import Scoreboard

print("Day 22 - 100 Days of Code.")
print("Welcome to Pong: The Famous Arcade Game.")

zero = 0
ten = 10
right_angle = 90
straight_angle = 180
turtle_helper = Turtle(visible=False)
screen = Screen()
screen.tracer(zero)
screen.setup(width=800, height=600)
screen.title("Pong: The Famous Arcade Game.")
screen.bgcolor("black")
turtle_helper.speed("fastest")
turtle_helper.pencolor("white")
turtle_helper.pensize(ten)
game_over = False


def create_borders():
    turtle_helper.penup()
    turtle_helper.goto(385, 290)
    turtle_helper.pendown()
    turtle_helper.right(right_angle)
    turtle_helper.forward(575)
    turtle_helper.right(right_angle)
    turtle_helper.forward(780)
    turtle_helper.right(right_angle)
    turtle_helper.forward(580)
    turtle_helper.right(right_angle)
    turtle_helper.forward(780)


def create_demarcation():
    turtle_helper.pensize(5)
    turtle_helper.penup()
    turtle_helper.goto(zero, 300)
    turtle_helper.setheading(270)
    turtle_helper.pendown()
    for iterator in range(59):
        if iterator % 2 == zero:
            turtle_helper.penup()
        else:
            turtle_helper.pendown()
        turtle_helper.forward(ten)


create_borders()
create_demarcation()
right_paddle = Paddle.Paddle(350)
left_paddle = Paddle.Paddle(-360)
scoreboard = Scoreboard.Scoreboard()
ball = Ball.Ball()

while not game_over:
    screen.update()
    time.sleep(0.05)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    # Detect collision with paddle.
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # Detect right paddle misses.
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    # Detect left paddle misses.
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()

    screen.listen()
    screen.onkey(right_paddle.move_paddle_up, key="Up")
    screen.onkey(right_paddle.move_paddle_down, key="Down")
    screen.onkey(left_paddle.move_paddle_up, key="w")
    screen.onkey(left_paddle.move_paddle_down, key="s")

    if scoreboard.right_score >= 1 or scoreboard.left_score >= 1:
        winner = ""
        game_over = True
        turtle_helper.penup()
        turtle_helper.goto(-110, zero)
        if scoreboard.right_score > scoreboard.left_score:
            winner = "RIGHT"
        else:
            winner = "LEFT"
        turtle_helper.write("GAME OVER!", font=("Courier", 30, "bold"))
        turtle_helper.goto(-170, -45)
        turtle_helper.write(f"WINNER: {winner}.", font=("Courier", 30, "bold"))

screen.exitonclick()
