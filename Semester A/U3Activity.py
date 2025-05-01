x = 10 #Integer
print("The variable 'x' is equal to", x)

y = float(input("Gice me a random decimal number. ")) #Float

z = x + y #Float
print("x plus y is equal to " + str(z))


mins = int(input("How many minutes were you on the phone for this month? "))
txts = int(input("How many text messages have you sent this month? "))

total = 0.1*mins+0.05*txts+8

print("Your total is: $" + str(total))