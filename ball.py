from turtle import Turtle
import random
TURN_ANGLES = [45, 135, 225, 315]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(random.choice(TURN_ANGLES))
        self.ball_speed = 0.1

    def move(self):
        self.forward(20)

    def bounce(self):
        if self.ycor() > 380:
            if self.heading() == TURN_ANGLES[0]:
                self.setheading(TURN_ANGLES[3])
            elif self.heading() == TURN_ANGLES[1]:
                self.setheading(TURN_ANGLES[2])
        elif self.ycor() < -380:
            if self.heading() == TURN_ANGLES[3]:
                self.setheading(TURN_ANGLES[0])
            elif self.heading() == TURN_ANGLES[2]:
                self.setheading(TURN_ANGLES[1])

    def hit_r_paddle(self):
        if self.heading() == TURN_ANGLES[3]:
            self.setheading(TURN_ANGLES[2])
        elif self.heading() == TURN_ANGLES[0]:
            self.setheading(TURN_ANGLES[1])
        self.ball_speed *= 0.9

    def hit_l_paddle(self):
        if self.heading() == TURN_ANGLES[2]:
            self.setheading(TURN_ANGLES[3])
        elif self.heading() == TURN_ANGLES[1]:
            self.setheading(TURN_ANGLES[0])
        self.ball_speed *= 0.9

    def refresh(self):
        self.goto(x=0, y=0)
        self.setheading(random.choice(TURN_ANGLES))
