import random

filePath = input("Please enter the file path for the text file that you want to open. ")
myFile = open(filePath, "r")
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
    
    # If its not a character that seperates words keep building the word
    # if paragraph[i] != " " and paragraph[i] != "." and paragraph[i] != ",":
    #     word = word+paragraph[i]
    # elif word != "":
    #     # Once word is equal to a set of letters then it will jumble the inside letters
    #     # print(word)
    #     # print(f"Word is '{word}'")
    #     print(jumble(word), paragraph[i], sep="", end="")
    #     word = ""

    if paragraph[i] == " " or paragraph[i] == "." or paragraph[i] == ",":
        
        if word != "":
            print(jumble(word), end="")
            word = ""
    
        print(paragraph[i], end="")
    else:
        word = word+paragraph[i]
    
print()