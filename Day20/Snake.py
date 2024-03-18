from turtle import Turtle

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
DOWN = 270
UP = ninety
RIGHT = zero
LEFT = one_hundred_and_eighty


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[zero]

    def start_up(self):
        for body_part in range(len(self.snake_body) - one, zero, -one):
            x_coordinate, y_coordinate = self.snake_body[body_part - one].pos()
            self.snake_body[body_part].goto((x_coordinate, y_coordinate))
        self.head.forward(twenty)
        if (self.head.pos()[zero] >= 285
                or self.head.pos()[one] >= 285
                or self.head.pos()[zero] <= -285
                or self.head.pos()[one] <= -285):
            return True

    def create_snake(self):
        for iterator in range(3):
            turtle = Turtle(shape="square")
            turtle.color("White")
            turtle.speed("fastest")
            turtle.penup()
            turtle.goto(zero - (iterator * twenty), zero)
            self.snake_body.append(turtle)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
