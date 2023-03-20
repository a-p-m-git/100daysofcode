import turtle
import random
import time


s = turtle.Screen()
s.setup(width=600,height=600)
s.tracer(0)
s.bgcolor("black")
s.title("sNake 0.0")



#TODO-1 CREATE SNAKE BODY

t_list = []
turtle_body_length = 3
start_x , start_y = 0,0

for i in range(turtle_body_length):
    t_list.append(turtle.Turtle("square"))
    t_list[i].color("white")
    t_list[i].penup()
    t_list[i].setposition(start_x,start_y)
    start_x -= 20

#TODO-2 MOVE THE SNAKE

running = True

while running:
    s.update()
    time.sleep(0.5)
    for dict in t_list:
        dict.fd(20)



#TODO-3 CREATE SNAKE FOOD

#TODO-4 DETECT COLLISION WITH FOOD

#TODO-5 CREATE A SCOREBOARD

#TODO-6 DETECT COLLISION WITH WALL

#TODO-7 DETECT COLLISION WITH TAIL




s.exitonclick()
