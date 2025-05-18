import turtle
import statistics

amount = int(input("How much does your item cost in cents?: "))
amountPaid = int(input("How much did you pay in cents?: "))

amountOwed = amountPaid - amount

def drawShape():
    Mark = turtle.Turtle()
    Mark.back(80)
    Mark.left(90)
    Mark.forward(50)
    Mark.right(90)
    Mark.forward(80)
    Mark.back(80)
    Mark.left(90)
    Mark.forward(50)
    Mark.right(90)
    Mark.forward(80)
    
drawShape()

turtle.done

inventory = ["medium", "small", "large"]
purchase = ""
medPurchased = False

if "medium" in inventory:
    print("Available")
    purchase = input("Do you want to purchase medium? ")
    if purchase in ["Yes", "yes", "y", "Y"]:
        medPurchased = True
        inventory.remove("medium")
    else:
        print("Okay!")
else:
    print("Sorry, out of stock")
    
num1 = 0
num2 = 0

numbers = []

numAverage = 0

num1 = int(input("Choose a number: "))
numbers.append(num1)
num2 = int(input("Choose another number: "))
numbers.append(num2)

numAverage = statistics.mean(numbers)

print(numAverage)