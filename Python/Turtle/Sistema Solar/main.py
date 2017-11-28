import turtle
turtle.shape("turtle")

turtle.penup()

#Sol

turtle.goto(0,0)
turtle.dot(50,"yellow")
turtle.write("Sol")


#Mercurio
turtle.penup()
turtle.goto(70,0)
turtle.dot(20,"brown")
turtle.left(90)
turtle.pencolor("brown")
turtle.pendown()
turtle.circle(70)
turtle.write("Mercurio")

#Venus
turtle.penup()
turtle.right(90)
turtle.goto(120,0)
turtle.dot(25,"green")
turtle.left(90)
turtle.pencolor("green")
turtle.pendown()
turtle.circle(120)
turtle.write("Venus")

#Tierra
turtle.penup()
turtle.right(90)
turtle.goto(160,0)
turtle.dot(35,"blue")
turtle.left(90)
turtle.pencolor("blue")
turtle.pendown()
turtle.circle(160)
turtle.write("Tierra")


