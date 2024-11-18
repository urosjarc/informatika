import turtle

def glavnik(stevilo):
  for i in range(0, stevilo, 1):
    turtle.left(90)
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(90)
    turtle.forward(100)

def lizike(stevilo):
  for i in range(0, stevilo, 1):
    turtle.left(90)
    turtle.forward(100)
    turtle.dot(10)
    turtle.backward(100)
    turtle.right(90)
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()

def zvezda(stevilo):
  stopinje = 360 / stevilo
  for i in range(0, stevilo, 1):
    turtle.forward(100)
    turtle.backward(100)
    turtle.left(stopinje)

def babuska(stevilo):
  a = 0
  for i in range(0, stevilo, 1):
    turtle.circle(a)
    a = a + 10

turtle.speed(-1)
babuska(10)
turtle.exitonclick()
