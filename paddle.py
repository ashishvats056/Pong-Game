from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.setheading(270)
        self.setposition(position)

    def move_up(self):
        self.backward(20)

    def move_down(self):
        self.forward(20)
