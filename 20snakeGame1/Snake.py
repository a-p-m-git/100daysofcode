class Snake:
    def __init__(self) -> None:
        pass

def 
#TODO-1 CREATE SNAKE BODY

t_list = []
turtle_body_length = 8
start_x , start_y = 0,0

for i in range(turtle_body_length):
    t_list.append(turtle.Turtle("square"))
    t_list[i].color("white")
    t_list[i].penup()
    t_list[i].setposition(start_x,start_y)
    start_x -= 20

#TODO-2 MOVE THE SNAKE

running = True

while running:
    s.update()
    time.sleep(0.1)
    
    print(t_list)
    
    for a in range(len(t_list) -1,0,-1):
        print(a)
        t_list[a].setposition(t_list[a - 1].xcor(),t_list[a - 1].ycor())
    
    t_list[0].fd(20)
    print(t_list[0].xcor())
    
    if t_list[0].xcor() >= 600:
        t_list[0].setheading(random.randint(0,360))
        t_list[0].write(t_list[0].xcor())
    elif t_list[0].xcor() == -600:
        t_list[0].setheading(0)
        t_list[0].write(t_list[0].xcor())   
   