import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########
tim.speed(0)
#tim.width(10)

for i in range(int(360 / 5)):
    tim.left(5)
    tim.color(random_color())
    tim.circle(100)