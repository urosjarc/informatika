import turtle

def glavnik():
  for i in range(0, 5, 1):
    turtle.left(90)
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(90)
    turtle.forward(100)

def lizike():
  for i in range(0, 5, 1):
    turtle.left(90)
    turtle.forward(100)
    turtle.dot(10)
    turtle.backward(100)
    turtle.right(90)
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()

def zvezda():
  for i in range(0, 8, 1):
    turtle.forward(100)
    turtle.backward(100)
    turtle.left(45)

def babuska():
  a = 0
  for i in range(0, 8, 1):
    turtle.circle(a)
    a = a + 10

babuska()
turtle.exitonclick()
