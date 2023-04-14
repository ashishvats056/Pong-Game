from turtle import Turtle
x = 10
y = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.x = 10
        self.y = 10
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_speed = 0.09

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1
        self.move_speed *= 0.8

    def reset_game(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.08
