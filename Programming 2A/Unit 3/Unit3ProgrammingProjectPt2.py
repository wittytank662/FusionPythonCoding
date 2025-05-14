# import random

# wholeNum = random.randint(1, 100)
# decimal = (random.randint(1,10))*0.1

# num = wholeNum+decimal

# print("The number you will be guessing the square root of is", num)

# guess = float(input(f"What do you think the square root of {num} is? "))

# r = num / guess

# guess = (guess +r)/2 
# print(guess)

# n = float(input("Please enter a number with a decimal: "))
# guess = n/2

# r = n/guess
# guess = (guess + r) / 2
# r = n/guess
# guess = (guess + r) / 2
# r = n/guess
# guess = (guess + r) / 2
# r = n/guess
# guess = (guess + r) / 2
# r = n/guess
# guess = (guess + r) / 2

# print(guess)

n = float(input("Please enter a number with a decimal: "))

guess = n / 2
previousGuess = 0

while abs(guess - previousGuess) > (0.01 * guess):
    previousGuess = guess
    r = n / guess
    guess = (guess + r) / 2
    
print(f"The square root of {n} is roughly {guess:.2f}")


# From Michael KIS - Keep It Simple



"""************************OUTPUT******************************


"""