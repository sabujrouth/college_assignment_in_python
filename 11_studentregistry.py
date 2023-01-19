# Write a python program to simulate a student registry with trivial operations. Records
# should be saved into a text file
import os

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"{self.name}, {self.age}, {self.grade}"

class Registry:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        for student in self.students:
            print(student)

    def save_to_file(self, file_name):
        with open(file_name, "w") as file:
            for student in self.students:
                file.write(str(student) + "\n")

# Initialize a new registry
registry = Registry()

# Add some students to the registry
registry.add_student(Student("Alice", 20, "A"))
registry.add_student(Student("Bob", 22, "B"))
registry.add_student(Student("Charlie", 21, "C"))

# Display all students in the registry
print("All students:")
registry.display_students()

# Save the registry to a file
file_name = "students.txt"
registry.save_to_file(file_name)
print(f"Registry saved to {file_name}")