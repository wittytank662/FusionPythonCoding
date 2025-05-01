import random

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
num3 = int(input("Please enter the third number: "))

if (num1 > (num2 and num3)):
    print("The first number is the largest.")
elif (num2 > (num1 and num3)):
    print("The second number is the largest.")
elif (num3 > (num1 and num2)):
    print("The third number is the largest")
elif (num1 == num2 == num3):
    print("All of the numbers are equal")


maxNum = 101
minNum = 1
secretNumber = int(input("Choose a number 1 through 100: "))
guessedNumber = 50
guesses = 0
maxGuesses = int(input("How many guesses do you want to give the computer?: "))


while (guessedNumber != secretNumber) and (guesses != maxGuesses):
    guesses += 1
    print("Is your number: ", str(guessedNumber)+"?")
    print("No? Aw okay!")
    if guessedNumber > secretNumber:
        maxNum = guessedNumber - 1
        guessedNumber = random.randrange(minNum, maxNum)
    if guessedNumber < secretNumber:
        minNum = guessedNumber + 1
        guessedNumber = random.randrange(minNum, maxNum)
if guessedNumber == secretNumber:
    print("Is your number: ", str(guessedNumber)+"?")
    print("woo! I win!")
    print("That took "+str(guesses)+" tries!")
else:
    exit()