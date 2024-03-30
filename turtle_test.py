import turtle as T
kame = T.Turtle()
screen = T.Screen()

a = 0

while a < 100:
    kame.forward(100)
    kame.left(140)
    a += 1


screen.exitonclick()

