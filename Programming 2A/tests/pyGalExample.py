import pygal

chart = pygal.Bar()
chart.title = "students Grades"
chart.x_labels = "Assignment 1", "Assignment 2", "Assignment 3", "Assignment 4"
chart.add("Student 1", [76, 72, 68, 64])

chart.render_to_file("grades.svg")