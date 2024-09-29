from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.list = []
        self.xmove = STARTING_MOVE_DISTANCE
        self.counter = True

    def generate_cars(self):
        car = Turtle("square")
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=3)
        car.color(random.choice(COLORS))
        if self.counter:
            car.goto(x=300, y=random.randint(-250, 300))
            self.counter = False
        else:
            self.change_pos(carango=car)
        self.list.append(car)
        self.move()

    def move(self):
        for cars in self.list:
            cars.goto(x=cars.xcor() - self.xmove, y=cars.ycor())

    def change_pos(self, carango):
        valid_pos = False
        while not valid_pos:
            new_y = random.randint(-250, 300)
            valid_pos = True
            for ruca in self.list:
                if ruca.distance(300, new_y) < 70:
                    valid_pos = False
                    break
        carango.goto(300, new_y)

    def increase_speed(self):
        self.xmove += MOVE_INCREMENT
