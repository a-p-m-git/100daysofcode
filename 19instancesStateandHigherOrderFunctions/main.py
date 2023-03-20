from turtle import Turtle, Screen
import random


screen = Screen()

screen.setup(width=500,height=400)

response = screen.textinput(title="MAKE YOUR BET!",prompt="Which turtle will win the race? Enter a colour: ")
turtle_colors = ["red","orange","yellow","green","blue","purple"]
turtle_list = []

# create turtles, set colors and initial coordinates
counter = 0
x, y = -250, 25
for color in turtle_colors:
  turtle_list.append(dict(name=color, turtle=Turtle("turtle")))
  turtle_list[counter]['turtle'].penup()
  turtle_list[counter]['turtle'].color(color)
  turtle_list[counter]['turtle'].speed(random.randint(1,10))
  turtle_list[counter]['turtle'].goto((x -20), y)
  counter+=1
  y += 20

#race turtles

for dict in turtle_list:
    dict['turtle'].forward(500)
    
    
    


print(turtle_list)


screen.exitonclick()