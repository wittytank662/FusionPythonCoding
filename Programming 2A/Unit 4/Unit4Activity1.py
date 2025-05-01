names = ["Liam", "Emma", "Noah", "Olivia", "Ava"]
grades = [85, 67, 92, 74, 59]

def selection_sort_names(name_list):
    for i in range(len(name_list)):
        min_index = i
        for j in range(i + 1, len(name_list)):
            if name_list[j] < name_list[min_index]:
                min_index = j
        
        name_list[i], name_list[min_index] = name_list[min_index], name_list[i]

def bubble_sort_grades(grade_list):
    n = len(grade_list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if grade_list[j] > grade_list[j + 1]:
                
                grade_list[j], grade_list[j + 1] = grade_list[j + 1], grade_list[j]

#Print original names ane grades
print("Original Names:", names)
print("Original Grades:", grades)

#Apply selection sort to names
selection_sort_names(names)
print("\nNames after Selection Sort (A-Z):", names)

#Apply bubble sort to grades
bubble_sort_grades(grades)
print("\nGrades after Bubble Sort (Low to High):", grades)

# Show students who pass
print("\nStudents who pass (grade >= 70):")
for i in range(len(grades)):
    if grades[i] >= 70:
        print(names[i], "-", "Grade:", grades[i])

print("\nStudnets who fail (grade < 70):")
for i in range(len(grades)):
    if grades[i] < 70:
        print(names[i], "-", "Grade:", grades[i])



'''
    I use lists because its easy to store multiple things,
    access items by their positions, and swap items easily.
    Lists also work well with selection sort and bubble sort.
'''