import random
from turtle import Turtle


class SnakeFood(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("orange")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.randomly_move_food()

    def randomly_move_food(self):
        """
        Description:
            Method to randomly generate food on screen for the snake.
        """
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
