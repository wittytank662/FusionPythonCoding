name = input("What is your name? ")
nameLower = (name.lower())
nameUpper = (name.upper())

print()
print("Your name in all lowercase is: ", nameLower)
print()
print("Your name in all uppercase is: ", nameUpper)
print()



print("Ages 21 and above are allowed into the park alone, 16 and above need a waiver, under 16 need to be with a parent or in a school group.")
age = int(input("How old are you? "))
if age >= 21:
    print("You are free to enter the water park.")
elif age >= 16:
    waiver = input("Do you have a waiver? ")
    if waiver in ["Yes", "yes", "Y", "y"]:
        print("You are free to enter the water park.")
    else:
        print("You are not allowed to enter the water park.")
elif age < 21:
    withAdult = input("Are you with an adult? ")
    if withAdult in ["Yes", "yes", "y", "Y"]:
        print("You are free to enter the water park.")
    else:
        withSchool = input("Are you with a school group? ")
        if withSchool in ["Yes", "yes", "y", "Y"]:
            print("You are free to enter the water park.")
        else:
            print("You are not allowed to enter the water park.")