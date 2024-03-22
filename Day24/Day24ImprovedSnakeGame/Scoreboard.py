from turtle import Turtle

zero = 0



class Scoreboard(Turtle):
    def __init__(self):
        # Adding mode to specifically allow permission to read. By default, it is read only.
        with open("snake_game_highscore.txt", mode="r") as highscore_file:
            self.highscore = int(highscore_file.read())
        self.score = zero
        super().__init__()
        self.hideturtle()
        self.print_score()

    def update_score(self):
        self.score += 1
        self.print_score()

    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("snake_game_highscore.txt", mode="w") as highscore_file:
                highscore_file.write(str(self.highscore))
        self.print_score()
        self.score = zero

    def print_score(self):
        self.clear()
        self.penup()
        self.goto(zero, 270)
        self.pendown()
        self.pencolor("White")
        self.write(f"Score: {self.score}. Highscore: {self.highscore}", align="center", font=("Courier", 15, "bold"))

