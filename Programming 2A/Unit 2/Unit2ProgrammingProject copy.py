import random

myFile = open("Unit2ProgrammingProject.txt", "r")
paragraph = myFile.readline()

def jumble(word):
    jumbledWord = ""
    firstLetter = word[0]
    middleLetters = word[1:-1]
    lastLetter = word[-1]
    
    jumbledWord += firstLetter
    
    count = 0
    letters = []
    for i in range(len(middleLetters)):
        letter = middleLetters[count]
        letters.append(letter)
        count = count + 1
        
    for i in range(len(letters)):
        num = random.randrange(len(letters))
        randLetter = letters[num]
        jumbledWord += randLetter
        letters.remove(randLetter)
        
    jumbledWord += lastLetter
    
    return jumbledWord

word = ""
for i in range(len(paragraph)): # This code breaks up the paragraph into the words, excluding the punctuation.
    if paragraph[i] != " " and paragraph[i] != "." and paragraph[i] != ",":
        word = word+paragraph[i]
    else:
        print(word)
        jumble(word)
        word = ""
