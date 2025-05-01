states = []

while True:

    menuOption = input("Do you want to append a state (a), remove a state (r), search for a state (s), modify a state (m), print the list (p), or quit the program (q)? ")

    if menuOption.lower() in ["a", "append"]:
        append = input("What state do you want to add to the list? ")
        states.append(append.lower())
        append = ""
    elif menuOption.lower() in ["r", "remove"]:
        remove = int(input("What position do you want to remove from the list? "))
        states.remove(remove)
        remove = None
    elif menuOption.lower() in ["s", "search"]:
        search = ""
        search = input("Enter what you want to search for: ")
        if search.lower() in states:
            pos = states.index(search) + 1
            print("That item is at position", pos)
        else:
            print("That is not in the list")
    elif menuOption.lower() in ["m", "modify"]:
        modify = input("What state do you want to modify? ")
        mPos = states.index(modify)
        
        modified = input("What do you want to change it to? ")
        states.remove(modify)
        states.insert(mPos, modified)
        modify = 0
        modified = ""
    elif menuOption.lower() in ["p", "print"]:
        print(states)
    else:
        quit()