from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("Blue")
        self.penup()
        self.shapesize(stretch_wid=0.75,stretch_len=0.75)
        self.position()

    def position(self):
        new_x=random.randint(-280,280)
        new_y=random.randint(-28,280)
        self.goto(x=new_x,y=new_y)
