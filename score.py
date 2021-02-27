from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.points = 0
        self.goto(x=0, y=370)
        self.color("yellow")
        self.write_score()

    def add_score(self):
        self.points += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=("Score: " + str(self.points)), align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
