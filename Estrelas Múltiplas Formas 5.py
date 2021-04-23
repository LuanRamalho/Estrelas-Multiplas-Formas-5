import turtle
a = turtle.Screen()
turtle.color('red', 'blue')
turtle.begin_fill()
grados = 0
turtle.speed(0)
for x in range(1, 40):
    for x in range(0, 4):
        turtle.forward(50)
        turtle.left(90)
    turtle.left(grados + 10)
turtle.end_fill()
a.exitonclick()
