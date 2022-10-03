from turtle import Turtle, Screen, colormode
from random import choice


colormode(255)
color_list = [(1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160),
              (242, 214, 69), (150, 84, 39), (215, 87, 64), (164, 162, 32),
              (158, 6, 24), (157, 62, 102), (11, 63, 32)
              ]
dot_radius = 20
dist_btw_dots = 50
x_pos = -225
y_pos = -225

tim = Turtle()
tim.shape("turtle")
tim.color("black", "green")
tim.speed("fastest")
tim.hideturtle()
tim.penup()
tim.setposition(x_pos, x_pos)
print(tim.pos())

for dot in range(10):
    for dot in range(10):
        tim.pencolor(choice(color_list))
        tim.dot(20)
        tim.forward(50)
    y_pos += dist_btw_dots
    tim.setposition(x_pos, y_pos)


screen = Screen()
screen.exitonclick()