class Student:
    count = 0

    def __init__(self, height=160):
        self.height = height
        Student.count += 1


print()
student = Student()
student1 = Student(height=170)
student2 = Student(height=150)
print(student.height)
print(student1.height)
print(student2.height)
print(student.count)
