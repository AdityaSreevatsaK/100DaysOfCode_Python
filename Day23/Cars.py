import random
from turtle import Turtle

from Scoreboard import Scoreboard

zero = 0
one = 1
two_hundred_and_fifty_five = 255

scoreboard = Scoreboard()


class Cars:
    def __init__(self):
        self.car_list = []
        self.speed = 5

    def generate_random_car(self):
        """
        Description:
            Method to randomly generate cars along the right-side y-axis.
        """
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            turtle = Turtle()
            turtle.shapesize(stretch_wid=one, stretch_len=2)
            turtle.penup()
            turtle.goto(280, random.randint(-250, 250))
            turtle.shape("square")
            turtle.color(random.random(), random.random(), random.random())
            turtle.setheading(180)
            self.car_list.append(turtle)

    def move_cars(self):
        """
        Description:
            Method to move the cars forward.
        """
        for car in self.car_list:
            car.forward(self.speed)
            if car.xcor() < -320:
                self.car_list.remove(car)

    def level_up(self):
        """
        Description:
            Method to increase the speed of the cars.
        """
        self.speed += 5
