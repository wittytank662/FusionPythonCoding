import random

print("Rolling a 6 sided die 10 times:")
for i in range(10):
    roll = random.randint(1, 6)
    print("Roll", i+1, ":", roll)