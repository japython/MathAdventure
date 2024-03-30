import turtle as T
kame = T.Turtle()
screen = T.Screen()

#kame.position(0,0)

num = int(input("how many?"))

def square(repeat):
    for a in range(repeat):
      kame.left(5)
      for i in range(4):
          kame.forward(100)
          kame.left(90)

#for i in range(4):
 #   kame.forward(150)
  #  kame.left(90)

square(num)

screen.exitonclick()