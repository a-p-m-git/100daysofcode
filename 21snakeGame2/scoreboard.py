from turtle import Turtle
import random

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.coords = (0,280)
        self.goto(self.coords)
        
    def update(self):
        self.score += 1
        
    def game_over(self):
        self.clear()
        self.coords = (0 - self.width(),0)
        self.goto(self.coords)
        self.write(f"GAME OVER!\nFinal Score: {self.score}")
    
    def print(self):
        self.clear()
        self.write("Score: " + str(self.score) )
