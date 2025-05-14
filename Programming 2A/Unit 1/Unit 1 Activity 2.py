myFile = open("movies.txt", "a")
more = input("Do you want to add a movie? enter 'yes' or 'no'. ")
while more.lower() == "yes":
    movie = input("Please enter a movie title: ")
    myFile.write(movie + "\n")
    more = input("Would you like to add another item? enter 'yes' or 'no'. ")
myFile.close()

found = False
count = 0
myFile = open("movies.txt", "r")
movies = myFile.readlines()
search = input("Do you want to search for a movie by the position? enter 'yes' or 'no'. ")
if search.lower() == "yes":
    number = int(input("Please enter the line number of the movie you want to find: "))
    print(movies[number - 1])
else:
    movieName = input("Please enter the name of the movie you want to search for: ")
    for line in movies:
        count = count + 1
        if movieName in line:
            print("The movies full title is: ", line, "on line", count)
            found = True    
    if found != True:
        print("That movie is not in the list.")
myFile.close()