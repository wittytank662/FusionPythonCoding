import random
import re
import pygal

collection = []
eyeColors = ["amber", "brown", "blue", "green", "hazel", "grey"]

# get user input on a persons name, age, phone number, zip code, and eye color.
for i in range(3):
    list = []
    name = ""
    age = 0
    phoneNum = 0
    zipCode = 0
    eyeColor = ""
    
    name = input("What is the first and last name of the person you want to add to the list? ")
    while name == "":
        name = input("You must enter the persons full name.")
    list.append(name)
    age = int(input("How old is the person? "))
    while age < 0 or age > 110:
        age = int(input("Please enter a valid age: ")) 
    list.append(age)
    phoneNum = input("What is their phone number? Enter in the format xxx-xxx-xxx: ")
    while not re.search("\d{3}-\d{3}-\d{4}", phoneNum):
        phoneNum = input("Please enter a valid phone number: ")
    list.append(phoneNum)
    zipCode = int(input("What is their zip code? "))
    while zipCode < 10000 or zipCode > 99999:
        zipCode = int(input("Please enter a valid zip code: "))
    list.append(zipCode)
    eyeColor = input("What is their eye color? ")
    while eyeColor.lower() not in eyeColors:
        eyeColor = input("Please enter a valid eye color: ")
    list.append(eyeColor)
    
    collection.append(list)

count = 0

print("NAME   AGE   PHONE NUMBER   ZIP CODE   EYE COLOR")
while count != 3:
    print(collection[count])
    count += 1

search = input("Would you like to search for someones phone number based on their name? ")
found = None

if search.lower() in ["yes", "y"]:
    searchedName = input("Please input the name you are searching: ")
    
    for sublist in collection:
        if searchedName in sublist:
            print("Their phone number is:", sublist[2])
            found = True
            break
        
    if not found:
        cont = input("That person is not in the list, do you want to continue searching? ")
        if cont.lower() not in ["yes", "y"]:
            exit()
            
createUsername = input("Do you want to create a username with your name? ")

if createUsername.lower() in ["yes", "y"]:
    usersName = input("What is your first and last name? ")
    
    username = (usersName.replace(" ", "")).lower()
    
    print("Your username is:", username)
else:
    pass

personOnesEyeColor = collection[0][4]
if personOnesEyeColor in eyeColors:
    eyeColors.remove(personOnesEyeColor)

newEyeColor = eyeColors[random.randrange(0, len(eyeColors))]

del collection[0][4]
collection[0].insert(4, newEyeColor)

print(collection[0][0], "has a new eye color.")
print(collection[0])

del collection[2][3]

print(collection[2][0], "no longer has a zip code.")
print(collection[2])


daysOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
pushups = [[50, 42, 37, 40, 45, 55, 24], [13, 27, 35, 24, 36, 47, 44], [30, 35, 33, 28, 23, 20, 18]]


chart = pygal.Line()

chart.title = "Pushups per day"

chart.x_labels = daysOfTheWeek

chart.add("Jackson", pushups[0])
chart.add("Dejuan", pushups[1])
chart.add("Darcy", pushups[2])

chart.render_to_file('pushups.svg')