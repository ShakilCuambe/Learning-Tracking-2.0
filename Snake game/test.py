    from turtle import Turtle, Screen
    turtle = Turtle()
    screen = Screen()
    screen.setup(width=600, height=600)
    turtle.goto(x=100, y=-120)
    sameda = Turtle()
    sameda.speed("lowest")
    sameda.goto(turtle)

    screen.exitonclick()