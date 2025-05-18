import turtle

myT = turtle.Turtle()

myT.speed(0)
for x in range(100):
    for i in range (3):
        myT.right(120)
        myT.forward(40)
    myT.right(3)
    myT.forward(3)
    

turtle.done()