num2 = None
while num2 == None:
  try:
    num1 = int(input("Please enter a dividend: "))
    num2 = int(input("Please enter a divisor: "))
    print("The result is: ", num1/num2)
  except:
    print("You cant divide by zero.")
    
#num1 = int(input("(2)Please enter a dividend: "))
#num2 = 0
#while num2 == 0:
    #try:
        #num2 = int(input("Please enter a divisor: "))
        #print("The result is: ", num1/num2)
    #except ZeroDivisionError:
        #print("The divisor must be non-zero.")    