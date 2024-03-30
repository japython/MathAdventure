import turtle as T
kame = T.Turtle()
kame.speed(3)
screen = T.Screen()

import random

def wander():

    while True:
        kame.fd(3)
        if kame.xcor() >= 200 or kame.xcor() <= -200 or kame.ycor() <= -200 or kame.ycor() >= 200:
            kame.lt(random.randint(90, 100))

wander()

screen.exitonclick()

