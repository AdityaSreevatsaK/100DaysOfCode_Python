from turtle import Turtle

twenty = 20


class Paddle(Turtle):
    def __init__(self, x_coordinate):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x_coordinate, 0)

    def move_paddle_up(self):
        """
        Description:
            Method to move the paddle up.
        """
        y_coordinate = self.ycor()
        if y_coordinate > 225:
            return
        self.goto(self.xcor(), y_coordinate + twenty)

    def move_paddle_down(self):
        """
        Description:
            Method to move the paddle down.
        """
        y_coordinate = self.ycor()
        if y_coordinate < -215:
            return
        self.goto(self.xcor(), self.ycor() - twenty)
