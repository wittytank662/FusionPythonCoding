import math

loop = True

while loop == True:
    
    def add(a, b):
        a + b
        return a + b
    def sub(a, b):
        endNum = a - b
        return endNum
    def mul(a, b):
        endNum = a * b 
        return endNum
    def div(a, b):
        if b == 0:
            return math.nan
        else:
            endNum = a / b
            return endNum

    def pwr(a, b):
        endNum = a**b
        return endNum

    def sqrt(a):
        endNum = math.sqrt(a)
        return endNum

    def collectInputs():
        input1 = int(input("Please input the first number: "))
        print()
        input3 = input("Do you want to add (add), subtract (sub), multiply (mul), divide (div), raise the number to the power of x (pwr), or find the square root of it (sqrt)? ")
        print()
        if input3 == "sqrt":
            pass
            input2 = 0
        else:
            input2 = int(input("Please input the second number: "))
        returnResults(input1, input2, input3)
        
    def returnResults(input1, input2, input3):
        if input3 == "add":
            print(str(input1)+" + "+str(input2)+" = "+str(add(input1, input2)))
        elif input3 == "sub":
            print(str(input1)+" - "+str(input2)+" = "+str(sub(input1, input2)))
        elif input3 == "mul":
            print(str(input1)+" * "+str(input2)+" = "+str(mul(input1, input2)))
        elif input3 == "div":    
            endNum = div(input1, input2)
            if endNum == math.nan:
                print("You can not divide by 0.")
            else:
                print(str(input1)+" / "+str(input2)+" = "+str(div(input1, input2)))
        elif input3 == "pwr":    
            print(str(input1)+" ^ "+str(input2)+" = "+str(pwr(input1, input2)))
        elif input3 == "sqrt":    
            print("The square root of "+str(input1)+" = "+str(sqrt(input1)))
        else:
            print("Error")
            
    collectInputs()
    
    loop = input("Do you want to continue? (y/n) ")
    if loop in ["y", "Y"]:
        loop = True
    else:
        loop = False