from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.hideturtle()
        self.print_score()

    def update_score(self):
        self.score += 1
        self.print_score()

    def print_score(self):
        self.clear()
        self.penup()
        self.goto(-30, 270)
        self.pendown()
        self.pencolor("White")
        self.write(f"Score: {self.score}", align="center", font=("Courier", 15, "normal"))
