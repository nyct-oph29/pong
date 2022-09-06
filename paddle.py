from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(1, 5)
        self.setheading(90)
        self.goto(position)

    def up(self):
        if self.ycor() < 360:
            self.forward(20)

    def down(self):
        if self.ycor() > -360:
            self.backward(20)
