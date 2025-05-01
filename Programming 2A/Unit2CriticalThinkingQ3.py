# Question 3

import time

def task1(i):
    print("Task 1 - Count", i)
    time.sleep(1)

def task2(i):
    print("Task 2 - Count", i)
    time.sleep(1)


for i in range(2): 
    task1(i)
    task2(i)

print("Both tasks completed!")
