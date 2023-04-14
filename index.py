from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from keep_score import Score
import time


def game_over():
    global game_on
    game_on = False


if __name__ == "__main__":
    POSITION_LEFT_PADDLE = (-350, 0)
    POSITION_RIGHT_PADDLE = (350, 0)
    game_on = True
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(height=600, width=800)
    screen.title("The famous pong game")
    screen.tracer(0)

    midline = Turtle()
    midline.setposition(0, 265)
    midline.setheading(270)
    midline.hideturtle()
    midline.color("white")
    for _ in range(18):
        midline.forward(20)
        midline.penup()
        midline.forward(10)
        midline.pendown()
    midline.forward(12)

    l_paddle = Paddle(POSITION_LEFT_PADDLE)
    r_paddle = Paddle(POSITION_RIGHT_PADDLE)
    score = Score()
    ball = Ball()
    screen.listen()
    screen.onkeypress(fun=l_paddle.move_up, key="w")
    screen.onkeypress(fun=l_paddle.move_down, key="s")
    screen.onkeypress(fun=r_paddle.move_up, key="Up")
    screen.onkeypress(fun=r_paddle.move_down, key="Down")
    screen.onkeypress(fun=game_over, key="space")
    screen.onkeypress(fun=screen.bye, key="x")

    while game_on:
        screen.update()
        time.sleep(ball.move_speed)
        ball.move()
        if ball.ycor() <= -280 or ball.ycor() >= 280:
            ball.bounce_y()
        if ball.distance(r_paddle) < 50 and ball.xcor() >= 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()
        if ball.xcor() > 400:
            ball.reset_game()
            score.increase_score_left()
        elif ball.xcor() < -400:
            ball.reset_game()
            score.increase_score_right()

    screen.exitonclick()
