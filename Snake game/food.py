                                                                                                                                                                                                                                                                                                                                                                                            from turtle import Turtle
                                                                                                                                                                                                                                                                                                                                                                                            import random
from snake import cores

BALLS = []
class Apple(Turtle) :
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.speed("fastest")
        self.goto(x=random.randint(-250, 250), y=random.randint(-280, 250))


    def change_pos(self, snake_parts):
        valid_position = False
        while not valid_position:  
            new_x = random.randint(-280, 280)
            new_y = random.randint(-280, 280)
            valid_position = True
           
            for part in snake_parts:
                if part.distance(new_x, new_y) < 20:
                    valid_position = False
                    break
        self.color(random.choice(cores))
        self.goto(new_x, new_y)





        
        
    
   
        
        