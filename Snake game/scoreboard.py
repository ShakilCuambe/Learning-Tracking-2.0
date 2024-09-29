from  turtle   import Turtle
from turtle import Turtle
from snake import cores

import random 

ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')

class Plakcard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(x=0, y=260)  # Move the score display to the top
        self.hideturtle()  # Hide the turtle cursor
        self.update_score()
        

    def update_score(self):
        """Clears the previous score and writes the new score."""
        self.clear()
        self.color(random.choice(cores))
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increases the score and updates the display."""
        self.score += 1
        self.update_score()

    def game_over(self):
        self.color("red")
        self.goto(x=0, y=0)
        self.write("Owari Da!", align=ALIGNMENT, font=FONT)