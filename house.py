import turtle

t = turtle.Turtle()
t.speed(3)

for i in range(4):
    t.forward(150)
    t.left(90)

t.left(45)
t.forward(106)
t.right(90)
t.forward(106)

t.penup()
t.goto(50, 0)
t.pendown()

t.left(45)
for i in range(2):
    t.forward(40)
    t.left(90)
    t.forward(25)
    t.left(90)

turtle.done()