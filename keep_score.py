from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.setposition(0, 270)
        self.write(arg="Current Score", align="center", font=("Arial", 16, "normal"))
        self.setposition(0, 240)
        self.write(arg=f"{self.l_score}      {self.r_score}", align="center", font=("Arial", 20, "normal"))

    def increase_score_left(self):
        self.l_score += 1
        self.update_score()

    def increase_score_right(self):
        self.r_score += 1
        self.update_score()
