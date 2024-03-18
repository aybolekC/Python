class Student:

    def __init__(self, ID, name, gpa):
        self.ID=ID
        self.name=name
        self.gpa=gpa
    
    def __repr__(self):
        return "Student = "+self.name


class Course:

    def __init__(self, name):
        self.name=name
        self.list_of_students=[]

    def add_a_student(self, student_obj):
        self.list_of_students.append(student_obj)

    def find_top(self):
        max_gpa=0
        top_student=None
        for student in self.list_of_students:
            if student.gpa> max_gpa:
                max_gpa=student.gpa
                top_student=student
        return top_student


student_A=Student(12,"Mary", 4)
student_B=Student(213,"Bob", 3)
student_C=Student(47,"Jill", 2.5)

mat_course=Course("Math")

mat_course.add_a_student(student_A)
mat_course.add_a_student(student_B)
mat_course.add_a_student(student_C)

print(mat_course.list_of_students)

top_student=mat_course.find_top()
print(top_student)