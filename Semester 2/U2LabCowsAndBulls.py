import random

secretNum = random.randint(1000, 9999)
bulls = 0
cows = 0
guesses = 0
gameRunning = True

print(secretNum)

def guessResults(secretNum, guess):
    cows = 0
    bulls = 0
    for i in range(len(str(secretNum))):
        if str(secretNum)[i] == str(guess)[i]:
            bulls += 1
        if str(guess)[i] in str(secretNum):
            cows += 1
    print("You have "+str(cows)+" cow (s) and "+str(bulls)+" bull (s).")

while gameRunning:
    guesses = 0
    guess = input("Choose a number 1000-9999: ")
    bullCount = guessResults(str(secretNum), guess)
    if bullCount == 4:
        print("You have succesfully guessed all 4 digits, you win!")
        gameRunning = False
    elif guesses <= 10:
        print("Try again!")
        guesses += 1
    elif guesses >= 10:
        print("You have run out of guesses.")
        gameRunning = False
        