from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("blue")
        self.goto(x=-220, y=240)
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"Level {self.score}", move=False, align="center", font=FONT)
        self.score += 1

    def game_over(self):
        self.color("red")
        self.goto(x=0, y=0)
        self.write("Owari Da!", align="center", font=FONT)
