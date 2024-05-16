from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.e_score = 0
        self.d_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.e_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 200)
        self.write(self.d_score, align="center", font=("Courier", 50, "normal"))
    def e_point(self):
        self.e_score += 1
        self.update_scoreboard()

    def d_point(self):
        self.d_score += 1
        self.update_scoreboard()
