'''
Classes ill need:

ExampleClass:
Attribute1, Attribute2, Attribute 3
Method1, Method2, Method3

Person:
Age, Name
about

Teacher:
name, age, gradeTeaching, classTimes, students
whosTakingTheClass, whatGradeDoITeach, about

Student:
name, age, grade, classes, gpa
whatGPA, about, whatClasses

OfficeStaff:
name, age, department, skills
staffsSkills, attendMeeting, completeTask, aboutStaff

Principal:
age, name, yearsWorked, schoolName
holdAssembly, evaluateTeacher, introduceSelf
'''

class Person:
    def __init__(self, age, name):
        self.__age = age
        self.__name = name
        
    def about(self):
        return f"{self.__name}'s is {self.__age} years old."
  
class Teacher(Person):
    def __init__(self, age, name, gradeTeaching, classTime, students):
        super().__init__(self, age, name)  
        
        self.__gradeTeaching = gradeTeaching    
        self.__classTime = classTime
        self.__students = students
        
    def about(self):
        return f"{self.__name} is {self.__age}."
        
    def whatGradeDoITeach(self):
        return f"{self.__name} teaches grade {self.__gradeTeaching} at {self.__classTime}."
    
    def whosTakingTheClass(self):
        return f"The students in the class are: {self.__students}"
        
class Student(Person):
    def __init__(self, age, name, grade, classes, gpa):
        Person.__init__(age, name)
        
        self.__grade = grade
        self.__classes = classes
        self.__gpa = gpa
        
    def about(self):
        return f"{self.__name} is {self.__age} years old and in grade{self.__grade}."
    
    def whatGPA(self):
        return f"{self.__name} has a {self.__gpa} GPA."
    
    def whatClasses(self):
        return f"{self.__name} is in these classes: {self.__classes}."
        
class OfficeStaff(Person):
    def __init__(self, age, name, department, skills):
        super().__init__(age, name)
        
        self.__department = department
        self.__skills = skills
        
    def aboutStaff(self):
        return f"{self.__name} is in the {self.__department} department."
        
    def staffsSkills(self):
        return f"{self.__name}'s skills are, {self.__skills}"
        
    def attendMeeting(self, topic):
        return f"{self.__name} is attending a meeting about {topic}."
    
    def completeTask(self, task):
        return f"{self.__name} has completed the task: {task}."
        
class Principal(Person):
    def __init__(self, age, name, yearsWorked, schoolName):
        super().__init__(age, name)
        
        self.__yearsWorked = yearsWorked
        self.__schoolName = schoolName
        
    def introduceSelf(self):
        return f"Hello, my name is {self.__name}, I am your new principal."
    
    def holdAssembly(self, topic):
        return f"{self.__name} is holding an assembly about {topic}."
        
    def evaluateTeacher(self, teacherName):
        return f"{self.__name} is evaluating {teacherName}'s work."

# Students - Age, Name, Grade, Classes, GPA
Alice = Student(19, "Alice", 13, ["History", "Chemistry", "Math", "English"], 3.9)
Brian = Student(16, "Brian", 11, ["History", "Science", "Math", "English"], 4.0)
Elena = Student(16, "Elena", 11, ["History", "Science", "Math", "English"], 2.9)
Frank = Student(17, "Frank", 11, ["History", "Science", "Math", "English"], 3.4)
Jacob = Student(18, "Jacob", 13, ["History", "Chemistry", "Math", "AP English"], 2.5)
Isla = Student(19, "Isla", 13, ["AP History", "Chemistry", "AP Physics", "English"], 3.9)

# Teachers - Age, Name, Grade teaching, Class time, Students
Carla = Teacher(37, "Carla", 11, 1, [Alice, Elena, Frank])
David = Teacher(42, "David", 13, 3, [Brian, Jacob, Isla])

# Office Staff - Age, Name, Department, Skills
Hassan = OfficeStaff(40, "Hassan", "Administration", ["Organization", "Multitasking"])
Grace = OfficeStaff(51, "Grace", "Attendance", ["Time managment", "Data entry"])
Liam = OfficeStaff(47, "Liam", "Counseling", ["Communication", "Empathy"])

# Principal - Age, Name, Years worked, School name
Kendra = Principal(62, "Kendra", 8, "Willow Creek")