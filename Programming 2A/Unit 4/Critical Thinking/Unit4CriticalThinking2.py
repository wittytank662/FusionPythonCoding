students = [
    ["Liam", 85],
    ["Olivia", 90],
    ["Noah", 78],
    ["Emma", 92]
]

searchName = input("Enter the students name: ")

found = False
for row in students:
    if row[0] == searchName:
        print(f"{searchName} found with grade {row[1]}")
        found = True
        break
    
if not found:
    print(f"{searchName} not found.")
    
