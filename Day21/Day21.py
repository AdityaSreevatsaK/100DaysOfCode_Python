import os
import time
from turtle import Screen, Turtle

import Scoreboard
import Snake
import SnakeFood

print("Day 21 - 100 Days of Code.")
print("Welcome to Snake Game!")

zero = 0
one = 1
ten = 10
twenty = 20
ninety = 90
one_hundred_and_eighty = 180
fastest_string = "fastest"
game_over = False
snake_body = []

snake = Snake.Snake()
snake_food = SnakeFood.SnakeFood()
scoreboard = Scoreboard.Scoreboard()
graphics_turtle = Turtle()
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game!")
screen.bgcolor("darkblue")
screen.tracer(zero)

graphics_turtle.pensize(ten)
graphics_turtle.pencolor("gold")
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


def end_game():
    """
    Description:
        Method to display that the game is over.
    """
    graphics_turtle.penup()
    graphics_turtle.goto(-ninety, zero)
    graphics_turtle.pendown()
    graphics_turtle.pencolor("White")
    graphics_turtle.write("Game Over! :(", font=("Palatino Linotype", 15, "italic"))
    print("Game over. Score:", scoreboard.score)


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


draw_borders(graphics_turtle)
graphics_turtle.hideturtle()
screen.listen()

screen.onkey(snake.turn_right, key="Right")
screen.onkey(snake.turn_left, key="Left")
screen.onkey(snake.turn_up, key="Up")
screen.onkey(snake.turn_down, key="Down")

while not game_over:
    screen.update()
    time.sleep(one / ten)
    if snake.start_up():
        end_game()
        game_over = True
    if snake_food.distance(snake.head) < 15:
        scoreboard.update_score()
        snake_food.randomly_move_food()
        snake.grow_tail(snake.snake_body[-1].pos())
    for body_part in snake.snake_body:
        if body_part == snake.head:
            pass
        else:
            if snake.head.distance(body_part) < 10:
                end_game()
                game_over = True
                break

screen.exitonclick()
