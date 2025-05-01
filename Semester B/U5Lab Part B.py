def fine(speed):
    if speed < 50 and speed > (-50):
        return 0
    elif speed > 100 or speed < (-100):
        return 300
    else:
        if speed > 0:
            extra = (speed - 50) / 5
            return 60 + 5 * extra
        elif speed < 0:
            extra = (speed + 50) / (-5)
            return 60 + 5 * extra

Repeating = None
while Repeating == None:
    try:
        userSpeed = int(input("Please enter your speed: ")) #Type Error
        Repeating = 1
    except ValueError:
        print("Please input a full number.")
print(fine(userSpeed))