
import turtle

loadWindow = turtle.Screen() 
kalem=turtle.Pen()
kalem.width(10)
kalem.speed(1)
kalem.shape("turtle")

kalem.color("red")
kalem.penup()
kalem.goto(-100,0)
kalem.pendown()
kalem.left(90)
kalem.forward(100)
kalem.right(315)
kalem.backward(141)
kalem.right(45)
kalem.forward(100)

kalem.penup()
kalem.goto(20,100)
kalem.pendown()
kalem.color("purple")

kalem.backward(100)
kalem.right(90)
kalem.forward(100)
kalem.left(90)
kalem.forward(100)

kalem.penup()
kalem.goto(140,0)
kalem.pendown()
kalem.color("pink")

kalem.forward(100)
kalem.right(90)
kalem.forward(60)
kalem.right(90)
kalem.forward(60)
kalem.right(90)
kalem.forward(50)
kalem.left(315)
kalem.backward(60)
import turtle
turtle.exitonclick() 
