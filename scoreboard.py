from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.ht()
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.update_sb()

    def update_sb(self):
        self.clear()
        self.goto(-200, 270)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(200, 270)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def left_point(self):
        self.l_score += 1
        self.update_sb()

    def right_point(self):
        self.r_score += 1
        self.update_sb()
