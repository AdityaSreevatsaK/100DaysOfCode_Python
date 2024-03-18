import time
from turtle import Screen, Turtle

import Snake

print("Day 20 - 100 Days of Code.")
print("Welcome to Snake Game!")

snake = Snake.Snake()

zero = 0
one = 1
ten = 10
twenty = 20
ninety = 90
one_hundred_and_eighty = 180
game_score = zero
fastest_string = "fastest"
game_over = False
snake_body = []
graphics_turtle = Turtle()
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game!")
screen.bgcolor("darkblue")
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
    print("Game over. Score:", game_score)


draw_borders(graphics_turtle)
graphics_turtle.hideturtle()
screen.tracer(zero)
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

screen.exitonclick()
