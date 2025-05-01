address = input("Please enter your address: ") ##String
addressLen = len(address) ##Int
fifthChar = address[4]
mainInAdd = False
addressWSpace = (address + " ")

print("Your address is", addressLen, "characters long.")


print("The fifth character of your address is: ", fifthChar)

if "Main" in address:
    mainInAdd = True
    print("Your address contains the word 'Main'")
else:
    mainInAdd = False
    print("Your address does not contain the word 'Main'")

print(addressWSpace * 3)