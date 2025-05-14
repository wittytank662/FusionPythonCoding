'''
import math

equation = input is your equation ax^2 - b^2 (1) or ax^2 - by^2 (2)

if equation is 1 then
    a = input what is a
    b = input what is b
    
    
    
    a = math.sqrt(a)
    b = math.sqrt(b)
    
    factored = f"({a}x - {b})({a}x + {b})"
    
    
    

else
    a = input what is a
    b = input what is b
    
    a = math.sqrt(a)
    b = math.sqrt(b)
    
    factored = (ax - by)(ax + by)


'''


# no need to use quadratic formula


import math

equation = int(input("Is your equation ax^2 - b^2 (1) or is it ax^2 - by^2 (2) "))

if equation == 1:
    a = int(input("Please input a: "))
    b = int(input("Please input b: "))
    
    a = math.sqrt(a)
    b = math.sqrt(b)
    
    factored = f"({a:.02f}x - {b:.02f})({a:.02f}x + {b:.02f})"
    print(factored)
    
else:
    a = int(input("Please input a: "))
    b = int(input("Please input b: "))
    
    a = math.sqrt(a)
    b = math.sqrt(b)
    
    factored = f"({a:.02f}x - {b:0.2f}y)({a:.02f}x + {b:0.2f}y)"
    print(factored)