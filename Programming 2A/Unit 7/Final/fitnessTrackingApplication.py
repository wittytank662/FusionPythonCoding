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
import os

header = ('''╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                               Fitness Tracker                                ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
''')

class Workout():
  def __init__(self, exercises, day):
    self.exercises = exercises
    self.day = day
    
  def addExercise(self, exercise):
    # Adds the exercise to the workout data
    self.exercises.append(exercise)
    
  def saveData(self):
    return str(self) + "\n"

    
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
  
  def __str__(self):
    setsStr = ", ".join(str(s) for s in self.sets)
    return f"Exercise: {self.exerciseName}, Sets: [{setsStr}]"
  
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
  with open("data.txt", "a") as file:
    file.write(workout.saveData())
  
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

def parseWorkoutLine(line):
  dayMatch = re.search(r"The workout on (.*?) is:", line)
  if not dayMatch:
    return None
  day =dayMatch.group(1)
  
  exercisePattern = r"Exercise: (.*?), Sets: \[(.*?)\](?:\.|,)"
  exerciseMatches = re.findall(exercisePattern, line)
  
  exercises = []
  for exName, setsStr in exerciseMatches:
    setPattern = r"Reps: (\d+), Weight: (\d+)"
    sets = [Set(int(r), int(w)) for r, w in re.findall(setPattern, setsStr)]
    exercises.append(Exercise(exName, sets))
  
  return Workout(exercises, day)

def searchWorkouts():
  userDate = input("Enter the workout date (MM/DD/YY): ").strip()
  
  parts = userDate.split("/")
  if len(parts) == 3:
    month = parts[0].zfill(2)
    day = parts[1].zfill(2)
    year = parts[2]
    userDate = f"{month}/{day}/{year}"
    
  found = False
  with open("data.txt", "r") as file:
    for line in file:
      if userDate in line:
        found = True
        print(f"Found workout for {userDate}:\n")
        
        exercisePattern = r"Exercise: (.*?), Sets: \[(.*?)\]\."
        matches = re.findall(exercisePattern, line)
        
        for name, setsStr in matches:
          print(f"Exercise: {name}")
          setEntries = re.findall(r"Reps: \d+, Weight: \d+", setsStr)
          for s in setEntries:
            print(f"  {s}")
        
  if not found:
    print("No workouts found for this day")

def addWorkoutUi():
    day = input("Enter workout day (MM/DD/YY): ").strip()
    workout = Workout([], day)
    
    while True:
        ex_name = input("Enter exercise name (or type 'done' to finish): ").strip()
        if ex_name.lower() == "done":
            break
        exercise = Exercise(ex_name, [])
        
        while True:
            try:
                reps = int(input(f"Enter number of reps for {ex_name}: "))
                weight = int(input(f"Enter weight used for {ex_name} (0 for bodyweight): "))
                exercise.addSet(Set(reps, weight))
            except ValueError:
                print("Please enter valid numbers.")
                continue
            
            more_sets = input("Add another set for this exercise? (y/n): ").strip().lower()
            if more_sets != "y":
                break

        workout.addExercise(exercise)
    
    print("\nWorkout summary:")
    print(workout)
    saveData(workout)
    
def editWorkout(dayInput):
  tempFile = "temp.txt"
  found = False

  parts = dayInput.split("/")
  if len(parts) == 3:
    month = parts[0].zfill(2)
    day = parts[1].zfill(2)
    year = parts[2]
    dayInput = f"{month}/{day}/{year}"

  with open("data.txt", "r") as readFile, open(tempFile, "w") as writeFile:
      for line in readFile:
          workout = parseWorkoutLine(line.strip())

          if workout and workout.day == dayInput:
              found = True
              print(f"Found workout on {dayInput}:")
              print(workout)

              if workout.exercises:
                  print("\nExercises:")
                  for i, ex in enumerate(workout.exercises):
                      print(f"{i + 1}. {ex.exerciseName}")
                  
                  try:
                      ex_choice = int(input("Select exercise to edit (number): ")) - 1
                      if 0 <= ex_choice < len(workout.exercises):
                          ex = workout.exercises[ex_choice]
                          print(f"Selected exercise: {ex.exerciseName}")
                          print("Current sets:")
                          for idx, s in enumerate(ex.sets):
                              print(f"{idx + 1}. {s}")

                          action = input("Would you like to (a)dd a new set or (d)elete an existing one? ").strip().lower()
                          if action == "a":
                              reps = int(input("Enter reps for new set: "))
                              weight = int(input("Enter weight for new set: "))
                              ex.addSet(Set(reps, weight))
                              print("Set added.")
                          elif action == "d":
                              del_idx = int(input("Enter set number to delete: ")) - 1
                              if 0 <= del_idx < len(ex.sets):
                                  removed = ex.sets.pop(del_idx)
                                  print(f"Removed set: {removed}")
                              else:
                                  print("Invalid set number.")
                          else:
                              print("Invalid action.")
                          print("Updated exercise:")
                          print(ex)
                      else:
                          print("Invalid exercise choice.")
                  except ValueError:
                      print("Invalid input. Must be a number.")

              writeFile.write(str(workout) + "\n")
          else:
              writeFile.write(line)

  if found:
      os.replace(tempFile, "data.txt")
      print(f"Workout on {dayInput} updated successfully.")
  else:
      os.remove(tempFile)
      print(f"No workout found on {dayInput}.")

def editWorkoutUi():
  day = input("Enter the workout day to edit (MM/DD/YY): ").strip()
  editWorkout(day)
  
def deleteWorkout():
  userDate = input("Enter the workout date (MM/DD/YY): ").strip()
  
  parts = userDate.split("/")
  if len(parts) == 3:
    month = parts[0].zfill(2)
    day = parts[1].zfill(2)
    year = parts[2]
    userDate = f"{month}/{day}/{year}"
    
  found = False
  with open("data.txt", "r") as file:
    
    lines = file.readlines()
    
    newLines = [line for line in lines if userDate not in line]
    
    if len(newLines) == len(lines):
      print("No workouts found for this day.")
      return
    
    delete = input(f"Are you sure you want to delete the workout for {userDate}? (y/n): ").lower()
    if delete == "y":
      with open("data.txt", "w") as file:
        file.writelines(newLines)
      print("Workout deleted.")
    else:
      print("Canceled.")
        
def mainMenu():
    while True:
        print(header)
        
        print('''╔════════════════════════════════════════════╗
║                 Main Menu                  ║
╠════════════════════════════════════════════╣
║ 1. Access Workouts                         ║
║ 2. Edit a Workout                          ║
║ 3. Add a Workout                           ║
║ 4. Delete a Workout                        ║
║ 5. Exit                                    ║
╚════════════════════════════════════════════╝''')
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            print("\n══ Access Workouts ══")
            searchWorkouts()
            input("\nPress Enter to return to the main menu...")
        elif choice == "2":
            print("\n══ Edit Workout ══")
            editWorkoutUi()
            input("\nPress Enter to return to the main menu...")
        elif choice == "3":
            print("\n══ Add Workout ══")
            addWorkoutUi()
            input("\nPress Enter to return to the main menu...")
        elif choice == "4":
          print("\n══ Delete Workout ══")
          deleteWorkout()
          input("\nPress Enter to return to the main menu...")
        elif choice == "5":
          print("Goodbye!")
          break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

# squatSet1 = Set(5, 80)
# squatSet2 = Set(5, 80)
# squatSet3 = Set(5, 80)
  
# squats = Exercise("Squats", [squatSet1, squatSet2, squatSet3])

# pushupSet1 = Set(5, 0)
# pushupSet2 = Set(5, 0)
# pushupSet3 = Set(5, 0)

# pushups = Exercise("Pushups", [pushupSet1, pushupSet2, pushupSet3])

# workout1 = Workout([pushups, squats], "01/10/10")

# print(workout1)

# saveData(workout1)

# loadWorkout()

# if __name__ == "__main__":
#   # Testing
#   setDebug = Set()
#   print(setDebug.stringToObject("Reps: 5, Weight: 0"))
  
#   loadSetFromLine()
  
# print(pushups)

# searchWorkouts()

mainMenu()
