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

class Workout():
  def __init__(self, exercises, day):
    self.exercises = exercises
    self.day = day
    
  def addExercise(self, exercise):
    # Adds the exercise to the workout data
    self.exercises.append(exercise)
    
  def saveData(self):
    # Saves the data in a .txt file
    pass
    
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
    return f"Exercise: {self.exerciseName}, Sets: {self.sets}."
  
  def __repr__(self):
    return self.__str__()
    
    
    
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
  
  def __str__(self):
    return f"Reps: {self.reps}, Weight: {self.weight}"
  
  def __repr__(self):
    return self.__str__()
    
squatSet1 = Set(5, 80)
squatSet2 = Set(5, 80)
squatSet3 = Set(5, 80)
  
squats = Exercise("Squats", [squatSet1, squatSet2, squatSet3])

pushupSet1 = Set(5, 0)
pushupSet2 = Set(5, 0)
pushupSet3 = Set(5, 0)

pushups = Exercise("Pushups", [pushupSet1, pushupSet2, pushupSet3])

workout1 = Workout([pushups, squats], "01/10/10")

print(workout1)