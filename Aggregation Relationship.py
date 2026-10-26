class Student:
    def __init__(self, name: str):
        self.name = name

    def __del__(self):
        print(f"Student object destroyed: '{self.name}'")

class Course:
    def __init__(self, students: list[Student] = None):
        # The Course accepts already-existing Student objects
        self.students = students if students else []

    def __del__(self):
        print("Course object destroyed.")


# --- Running the code ---
# 1. The students are created outside first, thus the students exist even if no course exists yet
student1 = Student("Alice")
student2 = Student("Bob")

# 2. Passed into the container class
my_course = Course([student1, student2])
print(f"Course populated with: {[s.name for s in my_course.students]}")

print("Executing: del my_course")
del my_course  # Wipes out the course object container

print("Checking variable accessibility after container deletion:")
print(f"Still active in memory -> student1: {student1.name}")
print(f"Still active in memory -> student2: {student2.name}")
# If 'my_course' is destroyed, student1 and student2 still live on in memory
