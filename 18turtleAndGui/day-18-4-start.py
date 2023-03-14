import turtle as t
import random

#TODO-1 Draw a triangle, square, pentagon, hexagon, heptagon, octagon, `
# nonagon and decagon. Each shape has a random color and sides-length of 100

screen_width = 1024
screen_height = 768

turtle_screen = t.Screen()
turtle_screen.screensize(screen_width,screen_height)
turtle_screen.colormode(255)
tim_turtle = t.Turtle()

randomRGB = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
tim_turtle.pencolor(randomRGB)

while turtle_screen.exitonclick():
    
    randomRGB = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    tim_turtle.pencolor(randomRGB)
    
    direction = random.randint(0,3)
    
    if direction == 0:
        

