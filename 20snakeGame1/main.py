import turtle
import random
import time
from Snake import Snake

s = turtle.Screen()
s.setup(width=600,height=600)
s.tracer(0)
s.bgcolor("black")
s.title("sNake 0.0")

running = True

#TODO-1 CREATE SNAKE BODY

snake = Snake()

s.listen()

s.onkey(snake.up,"Up")
s.onkey(snake.down,"Down")
s.onkey(snake.left,"Left")
s.onkey(snake.right,"Right")

#TODO-2 MOVE THE SNAKE


while running:
    s.update()
    time.sleep(0.1)
    
    
        
    snake.move()
#TODO-3 CREATE SNAKE FOOD

#TODO-4 DETECT COLLISION WITH FOOD

#TODO-5 CREATE A SCOREBOARD

#TODO-6 DETECT COLLISION WITH WALL

#TODO-7 DETECT COLLISION WITH TAIL

s.exitonclick()
