from turtle import Screen
from snake import Snake
from food import Apple
from scoreboard import Plakcard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("AntiqueWhite4")
screen.title("Tottenham")
screen.tracer(0)
screen.colormode(255)


scoreboard = Plakcard()
parts = []
snake = Snake(parts)
food = Apple()
snake.create_snake()


screen.listen()
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.down, key="s")
screen.onkey(fun=snake.right, key="d")
screen.onkey(fun=snake.left, key="a")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    snake.update_color()


    if snake.parts_list[0].distance(food) < 15:
        snake.add_part()
        food.change_pos(parts)
        scoreboard.increase_score()
        scoreboard.update_score()

    if snake.parts_list[0].xcor() > 280 or  snake.parts_list[0].xcor() < -280 or  snake.parts_list[0].ycor() > 280 or  snake.parts_list[0].ycor() < -280:
        game_on = False
        scoreboard.game_over()
    if snake.tail():
        game_on = False
        scoreboard.game_over()

screen.exitonclick()