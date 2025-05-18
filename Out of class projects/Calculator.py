inputOne = 0
symbol = "NaN"
inputTwo = 0
output = 0

inputOne = int(input("What is the first number? "))

while symbol not in ["+", "-", "*", "/"]:
    symbol = input("Are you adding (+), subtracting (-), multiplying (*), or dividing (/) ")
    if symbol not in ["+", "-", "*", "/"]:
        print("That is not a valid symbol")
        
inputTwo = int(input("What is the second number? "))

if symbol == "+":
    output = inputOne + inputTwo
    print(inputOne, symbol, inputTwo, "=", output)
elif symbol == "-":
    output = inputOne - inputTwo
    print(inputOne, symbol, inputTwo, "=", output)
elif symbol == "*":
    output = inputOne * inputTwo
    print(inputOne, symbol, inputTwo, "=", output)
elif symbol == "/":
    output = inputOne / inputTwo
    print(inputOne, symbol, inputTwo, "=", output)

# Simple calculator that only does addition, subtraction, multiplication, and division