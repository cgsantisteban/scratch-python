import turtle

screen = turtle.Screen()
screen.addshape("tierra2-cambiado.jpg")
screen.addshape("sol.jpg")


sol = turtle.Turtle()
sol.shape("sol.jpg")

tierra =turtle.Turtle()
tierra.shape("tierra2-cambiado.jpg")



tierra.penup()
tierra.goto(90,0)
tierra.left(90)
tierra.pendown()
tierra.speed(1)
tierra.pencolor("blue")
while True:
  tierra.circle(90)

#Repetir con cada uno de los planetas
# ....
