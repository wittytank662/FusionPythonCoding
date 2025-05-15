# Step 1
# Recursive Algorithm (Pseudocode)

'''
FUNCTION recursiveSum(array)
    IF array is empty THEN
        RETURN 0
    ELSE
        RETURN array[0] + recursiveSum(array[1:])
END FUNCTION
'''

# Step 2
# Recursive Algorithm (Python)

def recursiveSum(array):
    if len(array) == 0:
        return 0
    else:
        return array[0] + recursiveSum(array[1:])

# Test
print(recursiveSum([1, 2, 3, 4, 5])) # Output 15

# Step 3
# Iterative Solution (Python)

def iterativeSum(array):
    total = 0
    for num in array:
        total += num
    return total

# Test
print(iterativeSum([1, 2, 3, 4, 5])) # Output 15

# Step 4
# Libarary-based Solution (Python)

import math

def librarySum(array):
    return math.fsum(array)

# Test
print(librarySum([1, 2, 3, 4, 5])) # Output 15.0