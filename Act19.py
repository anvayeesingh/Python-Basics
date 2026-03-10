import turtle

t = turtle.Turtle()
t.color("red")
t.begin_fill()

t.left(140)
t.forward(180)

t.circle(-90,200)
t.left(120)

t.circle(-90,200)
t.forward(180)

t.end_fill()

t.penup()
t.goto(0,-180)

t.write("Happy Birthday Mom!", align="center", font=("Arial", 40, "bold"))

turtle.done()