'''
Classes ill need:

ExampleClass:
Attribute1, Attribute2, Attribute 3
Method1, Method2, Method3

Person:
Age, Name, Grade
printItems

Teacher:
name, gradeTeaching, classTimes, students, studentAmt
printGradeAndClass, takeAttendance

Student:
name, age, grade, classes, gpa
printItems

OfficeStaff:



Principal:


'''

class Person:
    def __init__(self, age, name):
        self.__age = age
        self.__name = name
        
    def printItems(self):
        print(f"{self.__name}'s is {self.__age} years old.")
  
class Teacher(Person):
    def __init__(self, age, name, gradeTeaching, classTimes, students):
        super().__init__(self, age, name)  
        
        self.__gradeTeaching = gradeTeaching    
        self.__classTimes = classTimes
        self.__students = students
        
    def printClassandGrade(self):
        print(f"{self.__name} teaches grade {self.__gradeTeaching} at {self.__classTimes}.")
        
    def whosInClass(self):
        print(f"The students taking the class are: {self.__students}.")
        
class Student(Person):
    def __init__(self, age, name, grade, classes, gpa):
        Person.__init__(age, name)

# class Student:
#     def __init__(self, grade, classes, gpa):
#         self.grade = grade
#         self.classes = classes
#         self.gpa = gpa
        
#     def printItems(self):
#         print(f"{self.name}'s is {self.age} years old and in grade {self.grade}.")
#         print(f"{self.name} is in these classes: {self.classes}")