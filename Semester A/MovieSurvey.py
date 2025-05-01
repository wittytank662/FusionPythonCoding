import csv

EightMile = 0

OldHenry = 0

lineCount = 0
choice = ""

while choice not in ["1", "2", "3"]:
    choice = input("What question would you like to see the answers for? (1, 2, 3): ")

with open("MovieSurvey.csv", mode='r') as myFile:
    reader = csv.reader(myFile)
    next(reader)
    for row in reader:
        lineCount += 1
        if row[2] == "Old Henry":
            OldHenry += 1
            
        if choice == "1":
            print("The results for question one are: ", row[1])
        elif choice == "2":
            print("The results for question two are: ", row[2])
        elif choice == "3":
            print("The results for question two are: ", row[3])



print("There were", lineCount, "submissions to this survey.")
print("There are", OldHenry, "people said that Old Henry was their favorite western.")