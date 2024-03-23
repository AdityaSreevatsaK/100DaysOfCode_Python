from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("orange")
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.5

    def move(self):
        """
        Description:
            Method to move the ball to a new position.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        Description:
            Method to bounce along the y-axis.
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        Description:
            Method to bounce along the x-axis.
        """
        self.x_move *= -1

    def reset_position(self):
        """
        Description:
            Method to reset the position of the ball.
        """
        self.goto(0, 0)
        self.bounce_x()
