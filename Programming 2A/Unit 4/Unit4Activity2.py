import math



# Algoritm

g = 32.2

dist = float(input("Enter the distance an object will fall (in feet): "))

time = math.sqrt((2 * dist) / g)

time = round(time, 1)

print("Time to fall:", time, "seconds.")


# Extended Algorithm

g = 32.2

distances = input("Enter distances in feet, seperated by commas: ")
distances = [float(d) for d in distances.split(",")]

times = []

for d in distances:
    t = math.sqrt((2 * d) / g)
    t = round(t, 1)
    times.append
    
print("\nTime for each object to fall: ")
for i in range(len(times)):
    print(f"Object {i+1}: {times[i]} seconds")
    
totalTime = sum(times)
print("\nTotal time to drop all items one after the other:", round(totalTime, 1), "seconds.")