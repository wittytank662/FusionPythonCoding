class Car:
    def __init__(self, company, model, color, releaseyear, speed=0):
        self.company = company
        self.model = model
        self.color = color
        self.releaseyear = releaseyear
        self.speed = speed
    
    def carAge(self, currentyear):
        return currentyear - self.releaseyear
    
    def repaint(self, newcolor):
        self.color = newcolor
        print(f"The car has been repainted to {newcolor}.")
        
    def accelerate(self, amount):
        self.speed += amount
        if self.speed < 0:
            self.speed = 0
        print(f"The car has accelerated by {amount} mph. Current speed: {self.speed} mph.")
        
    def brake(self, amount):
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0
        print(f"The car has slowed down by {amount} mph. Current speed: {self.speed} mph.")
        
    def __eq__(self, other):
        if isinstance(other, Car):
            return (self.company == other.company and
                    self.model == other.model and
                    self.releaseyear == other.releaseyear and
                    self.color == other.color)
            return False
        
Corolla1 = Car("Toyota", "Corolla", "Red", 1968, 60)
Corolla2 = Car("Toyota", "Corolla", "Red", 1968, 60)
Mustang = Car("Ford", "Mustang", "Black", 2020, 120)

print(f"Company: {Corolla1.company}")
print(f"Model: {Corolla1.model}")
print(f"Color: {Corolla1.color}")
print(f"Release Year: {Corolla1.releaseyear}")
print(f"Initial Speed: {Corolla1.speed}")

Corolla1.repaint("Blue")
Corolla1.repaint("Red")

age = Corolla1.carAge(2024)
print(f"The car is {age} years old.")

Corolla1.accelerate(50)
Corolla1.brake(25)

if Corolla1 == Corolla2:
    print("The first Corolla and the second Corolla are the same.")
else:
    print("The first Corolla and the second Corolla are different.")
    
if Corolla2 == Mustang:
    print("The second Corolla and Mustang are the same.")
else:
    print("The second Corolla and Mustang are different")