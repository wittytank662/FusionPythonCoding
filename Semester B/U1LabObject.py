import math

loop = True

while loop == True:
    

    class operations:
        def __init__(self, a, b):
            self.a = a
            self.b = b
            
        def addition(a, b):
            endNum = a + b
            return endNum
        
        def subtraction(a, b):
            endNum = a - b
            return endNum
        
        def multiplication(a, b):
            endNum = a * b
            return endNum
        
        def division(a, b):
            if b == 0:
                print("You cannot divide by 0")
            else:
                endNum = a / b
                return endNum
            
        def exponent(a, b):
            endNum = a ** b
            return endNum
        
        def square_root(a):
            endNum = math.sqrt(a)
            return endNum
        
    class calcStart:
        def __init__(self, input1, operation, input2, endNum):
            self.input1 = input1
            self.operation = operation
            self.input2 = input2
            self.endNum = endNum
                
        def inputs():
            input1 = int(input("Please input the first number: "))
            print()
            operation = input("Do you want to add (add), subtract (sub), multiply (mul), divide (div), raise the number to the power of x (pwr), or find the square root of it (sqrt)? ")
            print()
            if operation == "sqrt":
                input2 = math.nan
                pass
            else:
                input2 = int(input("Please input the second number: "))
            numbers = operations(input1, input2)
            return input1, operation, input2
            
        def results(input1, operation, input2, endNum):
            if operation == "add":
                print(str(input1)+" + "+str(input2)+" = "+str(endNum))
            elif operation == "sub":
                print(str(input1)+" - "+str(input2)+" = "+str(endNum))
            elif operation == "mul":
                print(str(input1)+" * "+str(input2)+" = "+str(endNum))
            elif operation == "div":
                print(str(input1)+" / "+str(input2)+" = "+str(endNum))
            elif operation == "pwr":
                print(str(input1)+" ^ "+str(input2)+" = "+str(endNum))
            elif operation == "sqrt":
                print("The square root of "+str(input1)+" = "+str(endNum))
            else:
                print("Error")
                

    input1, operation, input2 = calcStart.inputs()

    if operation == "add":
        endNum = operations.addition(input1, input2)
    elif operation == "sub":
        endNum = operations.subtraction(input1, input2)
    elif operation == "mul":
        endNum = operations.multiplication(input1, input2)
    elif operation == "div":
        endNum = operations.division(input1, input2)
    elif operation == "pwr":
        endNum = operations.exponent(input1, input2)
    elif operation == "sqrt":
        endNum = operations.square_root(input1)

    calcStart.results(input1, operation, input2, endNum)

    loop = input("Do you want to continue using the calculator? (y/n) ")
    if loop in ["y", "Y"]:
        loop = True
    else:
        loop = False