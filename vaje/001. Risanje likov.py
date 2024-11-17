import turtle
def kvadrat():
  for i in range(0, 4, 1):
    turtle.forward(100)
    turtle.left(90)

def crtice():
  for i in range(0, 10, 1):
    turtle.forward(100)
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()
def stopnice():
  for i in range(0, 10, 1):
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)

def spirala():
  stranica = 0
  for i in range(0, 100, 1):
    turtle.forward(stranica)
    turtle.left(90)
    stranica = stranica + 10

def kvadrati():
  stranica = 0
  for i in range(0, 100, 1):
    for j in range(0, 4, 1):
      turtle.forward(stranica)
      turtle.left(90)

    turtle.penup()

    turtle.back(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.left(90)

    turtle.pendown()
    stranica = stranica + 10

kvadrati()
turtle.exitonclick()
