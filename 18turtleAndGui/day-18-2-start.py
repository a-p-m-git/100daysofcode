import turtle

#TODO-1 DRAW A DASHED LINE FOR 10 PACES AND THEN A GAP OF 10 PACES 50 TIMES

screen_width = 1024
screen_height = 768

turtle_screen = turtle.Screen()
turtle_screen.screensize(screen_width,screen_height)
tim_turtle = turtle.Turtle()

for i in range(15):
  tim_turtle.forward(10)
  tim_turtle.penup()
  tim_turtle.forward(10)
  tim_turtle.pendown()

turtle_screen.exitonclick()