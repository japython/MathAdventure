import turtle as T
kame = T.Turtle()
screen = T.Screen()

#kame.position(0,0)

def triangle(length=100):
    for i in range(3):
        kame.forward(length)
        kame.left(120)

a = 0

While a < 100:

  num = int(input("how long?"))



#for i in range(4):
 #   kame.forward(150)
  #  kame.left(90)

  triangle(num)

  screen.exitonclick()