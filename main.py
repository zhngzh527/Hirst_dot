import colorgram
import turtle
import random

turtle.colormode(255)

# rgb_colors = []
#
# colors = colorgram.extract('hirst_dot.jpg', 12)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
#extract color from the picture and create the color's list

color_list = [(219, 173, 124), (159, 180, 190), (134, 73, 53), (49, 102, 153), (118, 82, 93), (179, 140, 150), (41, 46, 65), (162, 104, 151), (126, 173, 114)]

fei = turtle.Turtle()
turtle.mode('world')
turtle.setworldcoordinates(-1, -1, 20, 20)
fei.speed('fastest')
fei.penup()
fei.hideturtle()
number_dots = 100

for dot_count in range(1, number_dots + 1):
    fei.dot(40, random.choice(color_list))
    fei.fd(2)

    if dot_count % 10 == 0:
        fei.setheading(90)
        fei.forward(2)
        fei.setheading(180)
        fei.forward(20)
        fei.setheading(0)







screen = turtle.Screen()
screen.exitonclick()
