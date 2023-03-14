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

i = 10


for i in range(3,12):
    count = 0
    randomRGB = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    tim_turtle.pencolor(randomRGB)
    tim_turtle.pen(random.randint(110,150))
    while count < i: 
        tim_turtle.forward(100)
        tim_turtle.right(360 / i)
        tim_turtle.forward(100)
        count += 1
    
        
    
    



turtle_screen.exitonclick()
