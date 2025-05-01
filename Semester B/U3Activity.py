class Reminder:
    quantity = 0
    def __init__(self, length, name):
        self.length = float(length)
        self.name = name
        self.quantity += 1
    
    def rename(self, newName):
        self.name = newName
        
    def delay(self, newTime):
        if type(newTime) == str:
            print("That is not a valid number.")
        
        self.length += newTime
    


reminder01 = Reminder(0, "Take out trash")
reminder01.delay(int(input("How long until you should be reminded? (in hours)? ")))
reminder01.name = input("What do you want to call this reminder? ")

#print(reminder01.length)
#print(reminder01.name)

config = input("Do you want to configure the reminder (Y/N)? ")
if config in ["Y", "y"]:
    addTime = str(input("Do you want to add time to the reminder (negative time/pos time) (Y/N)? "))
    if addTime in ["Y", "y"]:
        reminder01.delay(int(input("How much longer do you want to add to the reminder (in hours)? ")))
        #print(reminder01.length)
    else:
        pass
    rename = input("Do you want to rename the reminder (Y/N)? ")
    if rename in ["Y", "y"]:
        reminder01.rename(input("What would you like to rename the reminder to? "))
        #print(reminder01.name)
    else:
        pass
else:
    pass

"""Remind michael to explain getters and setters - more advanced stuff.
"""