import turtle

def kvadrat(dolzina):
  for i in range(0, 4, 1):
    turtle.forward(dolzina)
    turtle.left(90)

def crtice(dolzina):
  for i in range(0, 10, 1):
    turtle.forward(dolzina)
    turtle.penup()
    turtle.forward(dolzina)
    turtle.pendown()

def stopnice(dolzina):
  for i in range(0, 10, 1):
    turtle.forward(dolzina)
    turtle.left(90)
    turtle.forward(dolzina)
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
