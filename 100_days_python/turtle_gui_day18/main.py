import turtle as turtle_module
import random 

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(202, 164, 189), (52, 93, 124), (223, 201, 135), (140, 30, 19), (238, 240, 245), (150, 75, 49), (124, 198, 221), (154, 213, 123), (127, 231, 125), (211, 209, 240), (123, 205, 109), (190, 234, 111), (190, 220, 123)]


tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100


for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)









screen = turtle_module.Screen()
screen.exitonclick()
















screen.exitonclick()