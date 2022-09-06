from turtle import Screen
from paddle import Paddle
import time
from scoreboard import ScoreBoard
from ball import Ball


screen = Screen()
screen.setup(width=1600, height=800)
screen.bgcolor("black")

screen.tracer(0)
paddle_one = Paddle((780, 0))
paddle_two = Paddle((-780, 0))
score = ScoreBoard()
ball = Ball()


screen.listen()
screen.onkeypress(fun=paddle_one.up, key="Up")
screen.onkeypress(fun=paddle_one.down, key="Down")
screen.onkeypress(fun=paddle_two.up, key="w")
screen.onkeypress(fun=paddle_two.down, key="s")

game = True
while game:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()
    ball.bounce()

    if ball.xcor() > 780 and ball.distance(paddle_one) < 50:
        ball.hit_r_paddle()
    elif ball.xcor() < -780 and ball.distance(paddle_two) < 50:
        ball.hit_l_paddle()

    if ball.xcor() > 800:
        ball.refresh()
        score.left_point()

    if ball.xcor() < -800:
        ball.refresh()
        score.right_point()

    if score.r_score >= 7 or score.l_score >= 7:
        score.goto(0,0)
        score.write("Game Over", align="center", font=("Courier", 24, "normal"))
        game = False


screen.exitonclick()
