import os
import time
from turtle import Screen, Turtle

import Scoreboard
import Snake
import SnakeFood

print("Day 24 Challenge - 100 Days of Code.")
print("Welcome to Improved Snake Game - With Highscore!")

zero = 0
one = 1
ten = 10
twenty = 20
ninety = 90
one_hundred_and_eighty = 180
fastest_string = "fastest"
game_over = False

snake = Snake.Snake()
snake_food = SnakeFood.SnakeFood()
scoreboard = Scoreboard.Scoreboard()
graphics_turtle = Turtle()
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game!")
screen.bgcolor("orangered4")
screen.tracer(zero)

graphics_turtle.pensize(ten)
graphics_turtle.pencolor("white")
graphics_turtle.speed(fastest_string)


def draw_borders(draw_turtle):
    """
    Description:
        Method to draw the borders for the snake game.
    """
    draw_turtle.penup()
    draw_turtle.goto(290, 300)
    draw_turtle.pendown()
    for _ in range(4):
        draw_turtle.right(ninety)
        draw_turtle.forward(590)
        draw_turtle.right(-ninety)
        draw_turtle.forward(one)
        draw_turtle.right(ninety)
    draw_turtle.penup()
    draw_turtle.goto(zero, zero)


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


def set_game_over():
    """
    Description:
        Method to set the game over variable to True.
    """
    global game_over
    game_over = True


draw_borders(graphics_turtle)
graphics_turtle.hideturtle()
screen.listen()
graphics_turtle.penup()
graphics_turtle.goto(zero, -270)
graphics_turtle.write("Press 'Enter' to exit.", align="center", font=("Courier", 15, "bold"))
screen.onkey(snake.turn_right, key="Right")
screen.onkey(snake.turn_left, key="Left")
screen.onkey(snake.turn_up, key="Up")
screen.onkey(snake.turn_down, key="Down")
screen.onkey(set_game_over, key="Escape")

while not game_over:
    screen.update()
    time.sleep(one / ten)
    if snake.start_up():
        scoreboard.reset_scoreboard()
        snake.reset_snake()
    if snake_food.distance(snake.head) < 15:
        scoreboard.update_score()
        snake_food.randomly_move_food()
        snake.grow_tail(snake.snake_body[-1].pos())
    for body_part in snake.snake_body:
        if body_part == snake.head:
            pass
        else:
            if snake.head.distance(body_part) < 10:
                scoreboard.reset_scoreboard()
                snake.reset_snake()
                break
print(f"Score: {scoreboard.score}. Highscore: {scoreboard.highscore}.")
screen.exitonclick()
