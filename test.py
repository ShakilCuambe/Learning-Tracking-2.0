from turtle import Turtle, Screen

screen = Screen()
timmy = Turtle("square")
yi= 0

for x in range(0, 50):
    timmy.goto(x=0, y=yi)
    yi +=20
    timmy = Turtle("square")

screen.exitonclick()
