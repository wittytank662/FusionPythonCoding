# Step 1
# Iterative Fibonacci Algorithm (Pseudocode)

'''
FUNCTION generateFibonacci(n)
    SET a = 0
    SET b = 1
    PRINT a
    PRINT b

    FOR i FROM 2 TO n - 1 DO
        SET next = a + b
        PRINT next
        SET a = b
        SET b = next
    END FOR
END FUNCTION
'''

# Step 2
# Iterative Fibonacci Algorithm (Python)

def generateFibonacci(n):
    if n <= 0:
        print("Please enter a positive number.")
        return
    
    fibList = []

    a, b = 0, 1

    for i in range(n):
        fibList.append(a)
        a, b = b, a + b

    print("Fibonacci numbers:", fibList)
    return fibList

# Test
fibNumbers = generateFibonacci(10) # Output [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Step 3
# Convert to binary

def toBinary(num):
    if num == 0:
        return '0'
    binary = ''
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    return binary

# Convert Fibonacci numbers to binary
binaryList = [toBinary(num) for num in fibNumbers]

print("Binary equivalents:", binaryList) # Output ['0', '1', '1', '10', '11', '101', '1000', '1101', '10101', '100010']