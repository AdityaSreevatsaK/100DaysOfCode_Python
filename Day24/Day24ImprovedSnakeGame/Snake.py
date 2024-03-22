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
        if (self.head.pos()[zero] >= 295
                or self.head.pos()[one] >= 295
                or self.head.pos()[zero] <= -295
                or self.head.pos()[one] <= -295):
            return True

    def create_snake(self):
        for position in [(zero, zero), (-twenty, zero), (-40, zero)]:
            self.grow_tail(position)

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

    def grow_tail(self, position):
        turtle = Turtle(shape="square", visible=False)
        turtle.speed("fastest")
        turtle.penup()
        turtle.goto(position)
        turtle.showturtle()
        turtle.color("White")
        self.snake_body.append(turtle)

    def reset_snake(self):
        for snake_body_part in self.snake_body:
            snake_body_part.hideturtle()
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[zero]
