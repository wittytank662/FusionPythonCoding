def grade(points):
    if points == 50:
        result = "D"
    elif points == 60:
        result = "C"
    elif points == 80:
        result = "B"
    elif points == 90:
        result = "A"
    else:
        result = "F"
    return result
        

score = int(input("How many points did you get on the assignment, out of 100? "))
print(grade(score))

