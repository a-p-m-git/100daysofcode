import turtle
import random
import time
import Snake

s = turtle.Screen()
s.setup(width=600,height=600)
s.tracer(0)
s.bgcolor("black")
s.title("sNake 0.0")

#TODO-1 CREATE SNAKE BODY

t_list = []
turtle_body_length = 8
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
    time.sleep(0.1)
    
    print(t_list)
    
    for a in range(len(t_list) -1,0,-1):
        print(a)
        t_list[a].setposition(t_list[a - 1].xcor(),t_list[a - 1].ycor())
    
    t_list[0].fd(20)
    print(t_list[0].xcor())
    
    if t_list[0].xcor() >= 600:
        t_list[0].setheading(random.randint(0,360))
        t_list[0].write(t_list[0].xcor())
    elif t_list[0].xcor() == -600:
        t_list[0].setheading(0)
        t_list[0].write(t_list[0].xcor())   
   

#TODO-3 CREATE SNAKE FOOD

#TODO-4 DETECT COLLISION WITH FOOD

#TODO-5 CREATE A SCOREBOARD

#TODO-6 DETECT COLLISION WITH WALL

#TODO-7 DETECT COLLISION WITH TAIL

s.exitonclick()
