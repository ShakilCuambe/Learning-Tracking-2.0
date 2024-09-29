from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player_turtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.left(90)
        self.penup()
        self.set_pos()
        self.penup()
        self.color("black")

    def go_forward(self):
        self.goto(x=self.xcor(), y=self.ycor() + MOVE_DISTANCE)

    def set_pos(self):
        self.goto(STARTING_POSITION)