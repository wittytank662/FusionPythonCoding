'''
needs exercises, reps, sets, duration, distance, laps, weight
Strength training: Workout > exercises > sets > reps > weight
Running: Distance > duration > laps >

Exercises needs to be a list
After choosing an exercise from the list you can add in your sets, reps, and the weight

needs to save in a txt file -- or somehow a sheet -- will figure out -- https://www.youtube.com/watch?v=X-L1NKoEi10 (Use Python To Import Data to Google Sheets)

'''

class strengthTraining():
    def __init__(self, exercises):
        self._exercises = exercises

    def listExercises(self):
        print(f"Youre exercises are: {self._exercises}")
        
list = []
for i in range(5):
    exercise = input("Add an exercise to the list: ")
    list.append(exercise)

workout1 = strengthTraining(list)
workout1.listExercises()