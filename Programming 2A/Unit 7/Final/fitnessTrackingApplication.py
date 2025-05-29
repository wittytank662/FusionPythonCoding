'''
Store in a text file, exercise, sets, reps, weight, day

search by day

workout = []

class Workout():

def addexercise()


class Exercise():

def addSet # Set will include reps

def setWeight # sets the weight that youve done for each set

class Sets() # set will be formatted like: "Reps: X, Weight: X"



'''
import re


class Workout():
  def __init__(self, exercises, day):
    self.exercises = exercises
    self.day = day
    
  def addExercise(self, exercise):
    # Adds the exercise to the workout data
    self.exercises.append(exercise)
    
  def saveData(self):
    # Saves the data in a .txt file
    return f"The workout on {self.day} is: {self.exercises}."
    
  def __str__(self):
    return f"The workout on {self.day} is: {self.exercises}."
  
  def __repr__(self):
    return self.__str__()


class Exercise():
  def __init__(self, exerciseName, sets):
    self.exerciseName = exerciseName
    self.sets = sets # Gonna be a list
    
  def addSet(self, whichSet):
    (self.sets).append(whichSet)
    return f"Your sets are now: {self.sets}"
  
  def saveData(self):
    return f"Exercise: {self.exerciseName}, Sets: {self.sets}."
  
  def __str__(self):
    return f"Exercise: {self.exerciseName}, Sets: {self.sets}."
  
  def __repr__(self):
    return self.__str__()
    
    
    
class Set():
  def __init__(self, reps = 0, weight = 0):
    self.reps = reps
    self.weight = weight
    
  def setReps(self, reps):
    self.reps = reps
    return f"This set now has {self.reps} reps."
      
  def stringToObject(self, string):
    reps = ""
    weight = ""
    
    for i in range(len(string)):
      
      if string[i:i+4] == "Reps":
        j = i + 6
        while string[j] != ",":
          reps += string[j]
          j += 1
          
      if string[i:i+6] == "Weight":
        j = i + 8
        while j < len(string) and string[j] not in [",", "]", "."]:
          weight += string[j]
          j += 1
          
    self.reps = int(reps)
    self.weight = int(weight)
    
    return f"Reps: {self.reps}, Weight: {self.weight}"
          

  def setWeight(self, weight):
    self.weight = weight
    return f"The new weight is now: {self.weight}"
  
  def saveData(self):
    return f"Reps: {self.reps}, Weight: {self.weight}"
  
  def __str__(self):
    return f"Reps: {self.reps}, Weight: {self.weight}"
  
  def __repr__(self):
    return self.__str__()
    
def saveData(workout):
  file = open("data.txt", "a")
  
  file.write(workout.saveData())
  file.write("\n")
  file.close()
  
def loadData():
  pass

def loadWorkout():
  file = open("data.txt", "r")
  
  exerciseString = file.readline()
  print(exerciseString)
    
def getSets(fullString):
  pattern = r"Reps: \d+, Weight: \d+"
  return re.findall(pattern, fullString)
    
def loadSetFromLine():
  lineNum = int(input("Enter the line number you want to read: "))
  with open("data.txt", "r") as file:
    lines = file.readlines()
    if 0 <= lineNum - 1 < len(lines):
      line = lines[lineNum - 1].strip()
      setsStrings = getSets(line)
      setsObjs = []
      for s in setsStrings:
        setObj = Set()
        setObj.stringToObject(s)
        setsObjs.append(setObj)
      for so in setsObjs:
        print(so)
    else:
      print("Invalid line number.")
    
squatSet1 = Set(5, 80)
squatSet2 = Set(5, 80)
squatSet3 = Set(5, 80)
  
squats = Exercise("Squats", [squatSet1, squatSet2, squatSet3])

pushupSet1 = Set(5, 0)
pushupSet2 = Set(5, 0)
pushupSet3 = Set(5, 0)

pushups = Exercise("Pushups", [pushupSet1, pushupSet2, pushupSet3])

workout1 = Workout([pushups, squats], "01/10/10")

# print(workout1)

# saveData(workout1)

# loadWorkout()

setDebug = Set()
print(setDebug.stringToObject("Reps: 5, Weight: 0"))

if __name__ == "__main__":
  # Testing
  setDebug = Set()
  print(setDebug.stringToObject("Reps: 5, Weight: 0"))
  
  loadSetFromLine()