# import colorgram
# colors = colorgram.extract("images/image.jpg", 25)
# li = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     li.append((r,g,b)) # rgb = first_color.rgb # e.g. (255, 151, 210)

# print(li)
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
colors = [
(46, 188, 231),(115, 121, 174),(75, 187, 126),(250, 66, 87),(4, 79, 35),(216, 137, 155),
(22, 78, 251),(72, 166, 205),(37, 116, 25),(72, 171, 106),(205, 217, 176),(97, 47, 243),(63, 72, 79),
(252, 55, 222),(156, 86, 199),(219, 248, 220),(176, 30, 209),
(53, 161, 57),(68, 237, 197),(252, 133, 240),(236, 59, 104),(203, 244, 189),(209, 3, 15),(95, 158, 254),(235, 135, 174)
]

y = -200

for i in range(10):
    tim.penup()
    tim.setposition(-200,y)
    for j in range(10):
        tim.pendown()
        tim.dot(20, random.choice(colors))
        tim.penup()
        tim.forward(40)
        
    y += 40



screen = t.Screen()
screen.exitonclick()