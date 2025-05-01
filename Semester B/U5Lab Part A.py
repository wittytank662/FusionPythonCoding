number = None

while number == None:
    
    try:
        number = int(input("Choose a number 1-10: "))
        if number >= 10 and number != 3720391:
            print("Please try again")
            number = None
        elif number <= 0:
            print("Please do not input a negative.")
            number = None
    except ValueError:
        print("That is not a valid number. Please try again.")
        
if number == 3720391:    
   print("Thank you. You have won a free toaster for choosing the right number!")
else:
    print("Thank you.")