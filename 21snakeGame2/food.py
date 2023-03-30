from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.shapesize(stretch_len=.5,stretch_wid=.5)
        self.speed("fastest")
        self.coords = (random.randint(-280,280),random.randint(-280,280))
        self.goto(self.coords)
        self.refresh()
        
    def refresh(self):
        self.coords = (random.randint(-280,280),random.randint(-280,280))
        self.goto(self.coords)
        