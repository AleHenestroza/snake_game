from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.high_score = 0
        self.color("yellow")
        self.write_score()

    def add_score(self):
        self.score += 1
        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(x=0, y=370)
        self.load_high_score()
        self.write(arg=f"Score: {self.score}       High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def load_high_score(self):
        with open("./data.txt") as data:
            self.high_score = int(data.read())
