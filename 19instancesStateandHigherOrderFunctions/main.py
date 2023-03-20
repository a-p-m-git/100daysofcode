from turtle import Turtle, Screen
import random


screen = Screen()

screen.setup(width=500,height=400)

response = screen.textinput(title="MAKE YOUR BET!",prompt="Which turtle will win the race? Enter a colour: ")
turtle_colors = ["red","orange","yellow","green","blue","purple"]
turtle_list = []
race_active = True

# create turtles, set colors and initial coordinates
counter = 0
x, y = -250, -75
for color in turtle_colors:
  turtle_list.append(dict(name=color, turtle=Turtle("turtle")))
  turtle_list[counter]['turtle'].penup()
  turtle_list[counter]['turtle'].color(color)
  #turtle_list[counter]['turtle'].speed(random.randint(1,10))
  turtle_list[counter]['turtle'].goto((x -20), y)
  counter+=1
  y += 20
  

#race turtles
while race_active:
  for dict in turtle_list:
    print(f"{dict['name']} {dict['turtle'].position()}")
    dict['turtle'].fd(random.randint(0,10))
    if (dict['turtle'].xcor() + 20) >= 400:
      print(f"{dict['name']} Wins!", end='')
      if response == dict['name']:
        print("You choose the Winner!")
      else:
        print("You choose the a loser")
        
      race_active = False
    
    

print(turtle_list)


screen.exitonclick()