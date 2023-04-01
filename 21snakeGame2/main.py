import turtle
import random
import time
from Snake import Snake
from food import Food
from scoreboard import Scoreboard

s = turtle.Screen()
s.setup(width=600,height=600)
s.tracer(0)
s.colormode(255)
s.bgcolor("black")
s.title("sNake 0.0")

running = True

#TODO-1 CREATE SNAKE BODY
#TODO-3 CREATE SNAKE FOOD

snake = Snake()
food = Food()
scoreboard = Scoreboard()

s.listen()

s.onkey(snake.up,"Up")
s.onkey(snake.down,"Down")
s.onkey(snake.left,"Left")
s.onkey(snake.right,"Right")




while running:
    s.update()
    time.sleep(0.2)
    scoreboard.print()    
    
    #TODO-2 MOVE THE SNAKE
    snake.move()
    

#TODO-4 DETECT COLLISION WITH FOOD
    if snake.t_list[0].distance(food) < 25:
        food.refresh()
        scoreboard.update()
        snake.extend()


#TODO-5 CREATE A SCOREBOARD
#see scoreboard.py

#TODO-6 DETECT COLLISION WITH WALL
    if snake.t_list[0].xcor() > 280 or snake.t_list[0].xcor() < -280:
        running = False
        scoreboard.game_over()
    elif snake.t_list[0].ycor() > 280 or snake.t_list[0].ycor() < -280:
        running = False
        scoreboard.game_over()


#TODO-7 DETECT COLLISION WITH TAIL

    for sn in snake.t_list:
        if sn == snake.t_list[0]:
            pass
        elif snake.t_list[0].distance(sn) < 10:
            running = False
            scoreboard.game_over()
        



s.exitonclick()
