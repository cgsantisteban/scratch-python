import turtle
turtle.shape("turtle")

#Sol
turtle.dot(80,"yellow")
turtle.write("Sol")

#Mercurio
turtle.penup()
turtle.goto(70,0)
turtle.left(90)
turtle.pendown()
turtle.pencolor("red")
turtle.circle(75)
turtle.dot(20,"red")
turtle.write("Mercurio")

#Venus
turtle.penup()
turtle.goto(120,0)
turtle.pendown()
turtle.pencolor("green")
turtle.circle(125)
turtle.dot(25,"green")
turtle.write("Venus")

#Tierra
turtle.penup()
turtle.goto(160,0)
turtle.pendown()
turtle.pencolor("blue")
turtle.circle(165)
turtle.dot(30,"blue")
turtle.write("Tierra")
