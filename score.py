from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=-40, y=270)
        self.points = 0

    def add_score(self):
        self.points += 1

    def write_score(self):
        self.clear()
        self.write(arg=("Score: " + str(self.points)), font=("Arial", 14, "normal"))
