
'''
 - Create a Classroom class that initializes with a subject name, and a list of students.
 - Create another class for Student that initializes with the student's name and gpa
 - The Classroom class should have methods that adds and removes students from the classroom list.
 - The Classroom class should have a method that returns the gpa average of all students in the classroom list.
 - The Student class should have a method that prints the student's name and gpa.
 - The Student class should have a method that updates the student's gpa
'''


class Student:

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __repr__(self):  # representation of the string
        return f'{self.name},{self.gpa}'

    def print_student_info(self):
        print(f'{self.name},{self.gpa}')

    def update_gpa(self, new_gpa):
        self.gpa = new_gpa


class ClassRoom:

    def __init__(self, subject_name: str):
        self.subject = subject_name
        self.students = []

    def __repr__(self):
        return self.subject

    def add_student(self, student: Student):
        self.students.append(student)

    def remove_student(self, name: str):
        for student in self.students:
            if name == student.name:
                s = self.students.index(student)  # returns the index of the student to remove
                del self.students[s]

    def get_gpa(self):
        total = 0
        for student in self.students:
            total = total + student.gpa
        average = total / len(self.students)
        return average


classroom = ClassRoom('Python')
s = Student('Jack', 4.0)
classroom.add_student(s)
print(classroom.students)
print(classroom)

