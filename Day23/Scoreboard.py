from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.speed("fastest")
        self.pencolor("purple2")

    def update_level(self):
        """
        Description:
            Method to update the level on screen.
        """
        self.clear()
        self.score += 1
        self.penup()
        self.goto(-280, 275)
        self.pendown()
        self.write(f"LEVEL: {self.score}", align="left", font=("Courier", 15, "normal"))
