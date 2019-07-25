
import turtle 
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
pen = turtle.Pen() 
turtle.bgcolor('black') 
for x in range(360): 
    pen.pencolor(colors[x%6]) 
    pen.width(x/100 + 1) 
    pen.forward(x)   #Moves the turtle forward by the specified amount
    pen.circle(5*x)  
    pen.right(60)    #Turns the turtle clockwise

