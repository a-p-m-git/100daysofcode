import turtle
import random
class Snake:
    def __init__(self) -> None:
        self.t_list = []
        self.t_body_len = 3
        self.t_start_x = 0
        self.t_start_y = 0

        self.create_body()
                
    def create_body(self):
        for i in range(self.t_body_len):
            self.t_list.append(turtle.Turtle("square"))
            self.t_list[i].color("white")
            self.t_list[i].penup()
            self.t_list[i].setposition(self.t_start_x,self.t_start_y)
            self.t_start_x -= 20

    def up(self):
        if self.t_list[0].heading() != 270:
            self.t_list[0].setheading(90)
    
    def down(self):
        if self.t_list[0].heading() !=90:
            self.t_list[0].setheading(270)
    
    def left(self):
        if self.t_list[0].heading() != 0:
            self.t_list[0].setheading(180)
    
    def right(self):
        if self.t_list[0].heading() != 180:
            self.t_list[0].setheading(0)
    
    
    def move(self):
        
        for a in range(len(self.t_list) -1,0,-1):
            self.t_list[a].setposition(self.t_list[a - 1].xcor(),self.t_list[a - 1].ycor())
        
        self.t_list[0].fd(20)
            
    def extend(self):
        temp_x, temp_y = self.t_list[len(self.t_list) - 1].xcor(), self.t_list[len(self.t_list) - 1].ycor()
        self.t_list.append(turtle.Turtle("square"))
        self.t_list[len(self.t_list) - 1].color("white")
        self.t_list[len(self.t_list) - 1].penup()
        self.t_list[len(self.t_list) - 1].setposition(temp_x,temp_y)
        