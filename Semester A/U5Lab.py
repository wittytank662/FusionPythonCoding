# Sequence

height = 0

height = input("How tall are you?: ")
print("Cool! you are "+str(height)+"cm tall!")

# Selection

if int(height) > 213:
    print("Wow! You are more than 7 feet tall!")
else:
    print("Wow! Very nice.")
    
# Iteration

password = ""
passwordlen = len(password)

while passwordlen < 8:
    password = str(input("Please enter your password: "))
    passwordlen = len(password)
    print(passwordlen)