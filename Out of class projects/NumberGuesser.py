import random

myNumber = 0
guessedNumber = random.randint(1, 10)
tries = 0
guessAgain = "NaN"

while not (1 <= myNumber <= 10):
    myNumber = int(input("Choose a number 1-10: "))
    if myNumber > 10 or myNumber < 1:
        print("That is not between 1 and 10.")

while True:
    print("Guessing...")
    print("Is your number..", guessedNumber)
    if guessedNumber == myNumber:
        print("That took me", tries, "tries!")
        break
    elif guessedNumber != myNumber:
        guessAgain = input("Aw man, can i try again? ")
        if guessAgain in ["Yes", "yes", "y", "Y"]:
            tries = tries + 1
            guessedNumber = random.randint(1, 10)
        elif guessAgain in ["No", "no", "n", "N"]:
            print("Okay! It was fun playing with you!")
            break

# Small number guesser