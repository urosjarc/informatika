import turtle

def mandala(stevilo):
  turtle.speed(-1)
  kot = 360 / stevilo
  for i in range(0, stevilo, 1):
    turtle.left(kot)
    turtle.circle(200)

def mreza_pik():
  for j in range(0, 10, 1):
    for i in range(0, 10, 1):
      turtle.dot(10)
      turtle.penup()
      turtle.forward(100)
      turtle.pendown()

    turtle.penup()
    turtle.backward(1000)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.pendown()

def mreza_crt():
    for i in range(10):
      turtle.forward(100)
      turtle.backward(100)
      turtle.left(90)
      turtle.forward(10)
      turtle.right(90)
      turtle.pendown()

    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.backward(100)

    for i in range(10):
      turtle.forward(100)
      turtle.backward(100)
      turtle.right(90)
      turtle.forward(10)
      turtle.left(90)
      turtle.pendown()

turtle.speed(2)
mreza_crt()
turtle.exitonclick()
