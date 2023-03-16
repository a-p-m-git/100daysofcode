###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import turtle as t
import colorgram
import random

color_list = [(149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), 
(145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), 
(147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

screen_width = 400
screen_height = 400

turtle_screen = t.Screen()
turtle_screen.screensize(screen_width,screen_height)
turtle_screen.colormode(255)
tim = t.Turtle()
#init_position = (-450,-350)
tim.penup()
tim.setposition(-(screen_width / 2), -(screen_height / 2))

    

#TODO-1 paint a painting of 10x10 randomly colour dots around 20 in circ and space by 50 

for _ in range(10):
    init_xcoord = tim.xcor()
    
    for i in range(10): 
        tim.penup()
        tim.setposition(tim.xcor() + 50,tim.ycor())
        tim.pendown()
        tim.dot(20,random.choice(color_list))

    tim.penup()
    tim.setposition(init_xcoord,tim.ycor() + 50) 
    
turtle_screen.exitonclick()