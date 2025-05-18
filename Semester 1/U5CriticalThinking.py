import random

a = 10
b = 40
c = 70
d = 90
x = a + b
y = c + d

print("The sum of 10 and 40 is "+str(x))
print("The sum of 70 and 90 is "+str(y))

totalRafTic = 1203
chosenNumbers = set()

winningRafTic1 = random.randrange(1, totalRafTic + 1)
chosenNumbers.add(winningRafTic1)

while True:
    winningRafTic2 = random.randrange(1, totalRafTic + 1)
    if winningRafTic2 not in chosenNumbers:
        chosenNumbers.add(winningRafTic2)
        break

while True:
    winningRafTic3 = random.randrange(1, totalRafTic + 1)
    if winningRafTic3 not in chosenNumbers:
        chosenNumbers.add(winningRafTic3)
        break

while True:
    winningRafTic4 = random.randrange(1, totalRafTic + 1)
    if winningRafTic4 not in chosenNumbers:
        chosenNumbers.add(winningRafTic4)
        break

while True:
    winningRafTic5 = random.randrange(1, totalRafTic + 1)
    if winningRafTic5 not in chosenNumbers:
        chosenNumbers.add(winningRafTic5)
        break

print("The first winning number is.. "+str(winningRafTic1))
print("The first winning number is.. "+str(winningRafTic2))
print("The first winning number is.. "+str(winningRafTic3))
print("The first winning number is.. "+str(winningRafTic4))
print("The first winning number is.. "+str(winningRafTic5))
