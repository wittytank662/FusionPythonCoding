class Box:
    def is_identical(self, other_box):
        return (self.date == other_box.date and
                self.contents == other_box.contents and
                self.location == other_box.location)

box1 = Box()
box1.date = "2024-10-23"
box1.contents = "Medical Records"
box1.location = "Room A"

box2 = Box()
box2.date = "2024-10-20"
box2.contents = "Syringes"
box2.location = "Room B"

box23 = Box()
box23.date = "2016"
box23.contents = "Medical records"
box23.location = "Storage closet"

box21 = Box()
box21.date = "2018"
box21.contents = "Lotion samples"
box21.location = "Waiting room"

box7 = Box()
box7.date = "2020"
box7.contents = "Flyers about the flu shot"
box7.location = "Receptionist's desk"

box10 = Box()
box10.date = "2020"
box10.contents = "Flyers about the flu shot"
box10.location = "Receptionist's desk"

print(box1.date, box1.contents, box1.location)
print(box2.date, box2.contents, box2.location)
print()
print("The contents of box 7 are:", box7.contents)
print("Box 21 is located in", box21.location)
print("The date of box 23 is:", box23.date)
print()
print("Box 7 date:", box7.date,"Box 7 contents:", box7.contents, "Box 7 location:", box7.location)
print("Box 10 date:", box10.date,"Box 10 contents:", box10.contents, "Box 10 location:", box10.location)
print()
print("Box 21 date:", box21.date,"Box 21 contents:", box21.contents, "Box 21 location:", box21.location)
print("Box 23 date:", box23.date,"Box 23 contents:", box23.contents, "Box 23 location:", box23.location)