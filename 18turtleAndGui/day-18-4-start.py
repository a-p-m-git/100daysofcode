import turtle as t
import random

#TODO-1 Draw a triangle, square, pentagon, hexagon, heptagon, octagon, `
# nonagon and decagon. Each shape has a random color and sides-length of 100

running = True

screen_width = 1024
screen_height = 768

turtle_screen = t.Screen()
turtle_screen.screensize(screen_width,screen_height)
turtle_screen.colormode(255)
tim_turtle = t.Turtle()
tim_turtle.pensize(12)
tim_turtle.speed(0)

while running:
    randomRGB = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    direction = random.randint(0,3)
    
    if direction == 0:
        tim_turtle.setheading(90)
    elif direction == 1:
        tim_turtle.setheading(270)
    elif direction == 2:
        tim_turtle.setheading(0)
    else:
        tim_turtle.setheading(180)
        
    tim_turtle.pencolor(randomRGB)
    tim_turtle.forward(50)

        

