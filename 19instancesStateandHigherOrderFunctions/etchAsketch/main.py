from turtle import Turtle, Screen


#TODO-1 CREATE A TURTLE THA RESPONDS TO W=FORWARD, S=BACKWARDS, A=COUNTER-CLOCKWISE , D=CLOCKWISE

running = True


tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_clockwise():
    #tim.right(10)
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def move_count_clockwise():
    #tim.left(10)
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def clear_screen():
    screen.resetscreen()
    
    


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_count_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
