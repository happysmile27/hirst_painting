# import colorgram
#
# color = colorgram.extract("hirst.jpg", 20)
# rgb_color = []
# for i in color:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
#
# print(rgb_color)
from turtle import Turtle, Screen
import random
screen = Screen()
screen.colormode(255)
turt = Turtle()
turt.speed("fastest")
turt.hideturtle()
colors = [(241, 250, 246), (142, 163, 184), (204, 137, 167), (192, 174, 15), (148, 16, 31), (68, 23, 31), (16, 139, 58), (237, 212, 66), (216, 160, 93), (50, 28, 26), (122, 71, 101), (198, 66, 28), (6, 107, 64), (228, 168, 197), (243, 216, 3), (25, 179, 89)]
turt.penup()
y = -200
step = 0
turt.setposition(-250, y)

for _ in range(10):
    for _ in range(10):
        turt.pendown()
        turt.dot(20, random.choice(colors))
        turt.penup()
        turt.forward(50)
    step += 50
    turt.setposition(-250, y + step)


# for y in range(-250, 250, 50):
#     for x in range(-250, 250, 50):
#         turt.goto(x, y)
#         turt.pendown()
#         turt.dot(20, random.choice(colors))
#         turt.penup()
#         turt.forward(50)

screen.exitonclick()
print(turt)