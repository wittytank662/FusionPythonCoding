import math
import pygal

numbers = []

print("Please enter 10 integers.")

for i in range(10):
    num = int(input("Enter an integer: "))
    numbers.append(num)
    
def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

primeNumbers = [num for num in numbers if prime(num)]
print("The prime numbers in the list are:", primeNumbers)

gcdFirstSecond = math.gcd(numbers[0], numbers[1])
print("The greatest common divisor between the first and second number are:", gcdFirstSecond)

squareThird = numbers[2] ** 2
print("The square of the 3rd number is:", squareThird)

sqrtEight = math.sqrt(numbers[7])
print("The square root of the eighth number is:", sqrtEight)

absTen = abs(numbers[9])
print("The absolute value of the tenth number is:", absTen)

decimalNumber = float(input("Please enter a decimal: "))
roundedDecimal = round(decimalNumber, 2)
numbers[3] = roundedDecimal
print("The fourth number in the list has been replaced with:", numbers[3])

expressionRes = (numbers[4] * numbers[2] // numbers[0]) + numbers[6]
numbers[5] = expressionRes
print("The sixth number in the list has been replaced with:", numbers[5])

print("The final list after all operations:", numbers)

lineChart = pygal.Line()
lineChart.title = "Numbers Line Chart"
lineChart.add("Numbers", numbers)
lineChart.render_to_file("U7activity.svg")

class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items ==[]
    
    def printStack(self):
        tempStack = self.items.copy()
        
        while tempStack:
            print(tempStack.pop())
            
myStack = Stack()

print(myStack.isEmpty())

myStack.push("apples")
myStack.push("bananas")
myStack.push("cheese")
myStack.push("doughnuts")
myStack.push("eggs")

print(myStack.isEmpty())

print("The size of the stack is: " + str(myStack.size()))

print(myStack.pop())

print("After popping an element, the size of the stack is: " + str(myStack.size()))

print("Stack contents:")
myStack.printStack()