import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
num_sides = 6
side_lenght = 70
angle = 360.0/num_sides
polygon = turtle.Turtle()
for i in range(num_sides):
    polygon.forward(side_lenght)
    polygon.right(angle)

turtle.done()