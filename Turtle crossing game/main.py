import time
from turtle import Screen
from player import Player_turtle
from car_manager import CarManager
from scoreboard_turtle import Scoreboard

cont = 1
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

scoreboard = Scoreboard()
managerc = CarManager()
player = Player_turtle()

screen.listen()
screen.onkey(fun=player.go_forward, key="w")

game_on = True
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if cont % 3 == 0:
        managerc.generate_cars()
    cont += 1
    managerc.move()

# winning condition
    if player.ycor() > 280:
        scoreboard.update()
        player.set_pos()
        managerc.increase_speed()


# Game over condition
    for enemy in managerc.list:
        if player.distance(enemy) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
