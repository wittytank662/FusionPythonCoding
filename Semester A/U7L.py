import turtle
    
Mark = turtle.Turtle()
Mark.speed(1)
startPos = Mark.pos()
# Floor
Mark.back(100)
# Left Wall
Mark.left(90)
Mark.forward(100)
# Left Roof
Mark.setheading(45)
Mark.forward(70.71)
# Right Roof
Mark.setheading(315)
Mark.forward(70.71)
# Right Wall
Mark.setheading(270)
Mark.forward(100)
# Door
Mark.setheading(180)
Mark.forward(35)
Mark.right(90)
Mark.forward(60)
Mark.left(90)
Mark.forward(30)
Mark.left(90)
Mark.forward(60)
# Doorknob
Mark.teleport(-60, 35)
Mark.circle(3)
# Window
Mark.teleport(-35, 75)
Mark.right(90)
Mark.forward(30)
Mark.right(90)
Mark.forward(30)
Mark.right(90)
Mark.forward(30)
Mark.right(90)
Mark.forward(30)
Mark.right(90)
Mark.forward(15)
Mark.right(90)
Mark.forward(30)
Mark.right(90)
Mark.forward(15)
Mark.right(90)
Mark.forward(15)
Mark.right(90)
Mark.forward(35)

endPos = Mark.pos()

print(startPos)
print(endPos)