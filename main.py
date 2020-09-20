import turtle
import math
turtle.penup()
turtle.right(90)
turtle.forward(200)
turtle.left(90)
turtle.pendown()
turtle.pencolor("orange")
turtle.circle(200)
turtle.penup()
turtle.setpos(0,0)
turtle.pendown()
turtle.color("red", 'red')
nose = 30
turtle.begin_fill()
turtle.forward(nose / 2)
turtle.right(135)
turtle.forward(nose)
turtle.right(90)
turtle.forward(nose)
turtle.right(135)
turtle.forward(nose * 1.5)
turtle.end_fill()

turtle.done()

# screen.textinput("NIM", "Name of first player:")
