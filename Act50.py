import turtle
u = turtle.Screen()
u.bgcolor("light blue")
u.title("Turtle")
q = turtle.Turtle()
size = 0
while True:
    for i in range(4):
        q.fd(size + 1)
        q.left(90)
        size = size - 5
    size = size+1