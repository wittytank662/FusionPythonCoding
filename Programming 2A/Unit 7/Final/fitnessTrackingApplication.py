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
exercises = []

class Workout():
  def __init__(self, exercise, day):
    self.exercises = exercise
    self.day = day
    
  def addExercise(self, exercise):
    # Adds the exercise to the workout data
    exercises.append(self.exercise)
    
  def saveData(self):
    # Saves the data in a .txt file
    pass
  
  def printWorkout(self):
    # Prints the workout data
    print(f"The workout is: {exercises}") # this is a no no
    
  def __str__(self):
    return f"The workout is: {exercises}"


class Exercise():
  def __init__(self, exerciseName, sets):
    self.exerciseName = exerciseName
    self.sets = sets # Gonna be a list
    
  def addSet(self, whichSet):
    (self.sets).append(whichSet)
    return f"Your sets are now: {self.sets}"
  
  def __str__(self):
    return f"Exercise: {self.exerciseName}, Sets: {self.sets}."
    
    
    
class Set():
  def __init__(self, reps, weight):
    self.reps = reps
    self.weight = weight
    
  def setReps(self, reps):
    self.reps = reps
    return f"This set now has {self.reps} reps."
      
  
  def setWeight(self, weight):
    self.weight = weight
    return f"The new weight is now: {self.weight}"
    
set1 = set(5, 80)
set2 = set("five")
set3 = set("four")
set4 = set("three")
  
squats = Exercise("Squats", [set1, set2, set3])

print(squats.addSet(set4))



  
  

# def addExercise():
#   # need to add an exercise name, the sets, and then reps.
#   exercise = []
#   exercise.append(input("What exercise did you do: "))
#   exercise.append(input("How many sets did you do: "))
#   exercise.append(input("How many reps did you do: "))
#   exercise.append(input("How much weight did you have: "))
#   exercise.append(input("What day was this? (xx/xx/xx): "))