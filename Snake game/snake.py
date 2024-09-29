from turtle import Turtle
import random
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
COL_DISTANCE = 10
cores = [(252, 251, 246), (253, 247, 251), (
    236, 251, 243), (200, 10, 35), (247, 236, 37), 
         (240, 244, 251), (239, 231, 3), (36, 216, 77), 
         (223, 159, 61), (39, 79, 185), (28, 39, 159), (210, 73, 16), 
         (17, 151, 18), (239, 39, 152), (65, 9, 27), (188, 14, 9), (216, 25, 127), 
         (218, 140, 198), (223, 161, 7), (59, 12, 7), (67, 202, 227), (10, 96, 60), 
         (84, 80, 212), (17, 19, 52), (237, 157, 218), (106, 232, 195), (99, 205, 136),
         (212, 84, 58), (8, 222, 235), (236, 171, 161)]

class Snake:
    def __init__(self, p_list):
        self.x = 0
        self.parts_list = p_list

    def create_snake(self):
        for _ in range(3):
            snake = Turtle(shape="square")
            snake.speed("fastest")
            snake.penup()
            snake.color(random.choice(cores))
            snake.shapesize(stretch_len=0.7, stretch_wid=0.7)
            snake.goto(x=self.x, y=0)
            self.x -= 20  # Decrementa para espacar as partes
            self.parts_list.append(snake)

    def move(self):
        for parts_num in range(len(self.parts_list) - 1, 0, -1):
            self.parts_list[parts_num].goto(self.parts_list[parts_num - 1].pos())
        self.parts_list[0].forward(MOVE_DISTANCE)

    def tail(self):
        # Verifica colisão com a cabeca a partir da segunda parte do corpo
        for tail in self.parts_list[1:]:
            if self.parts_list[0].distance(tail) < COL_DISTANCE:
                return True
        False

    def add_part(self):
        snake = Turtle(shape="square")
        snake.penup()
        snake.speed("fastest")
        snake.color(random.choice(cores))
        snake.shapesize(stretch_len=0.7, stretch_wid=0.7)
        # Adiciona a nova parte no final da cobra
        snake.goto(self.parts_list[-1].position())
        self.parts_list.append(snake)


    def update_color(self):
        for cobra in self.parts_list[1:]:  # Slice from index 1 to avoid changing the head color
            cobra.color(random.choice(cores))
            

    def up(self):
        if self.parts_list[0].heading() != DOWN:
            self.parts_list[0].setheading(UP)

    def down(self):
        if self.parts_list[0].heading() != UP:
            self.parts_list[0].setheading(DOWN)

    def right(self):
        if self.parts_list[0].heading() != LEFT:
            self.parts_list[0].setheading(RIGHT)

    def left(self):
        if self.parts_list[0].heading() != RIGHT:
            self.parts_list[0].setheading(LEFT)
