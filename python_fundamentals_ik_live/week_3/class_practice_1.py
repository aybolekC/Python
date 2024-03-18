# Create a new class
class Student:
    
    # Define a constructor
    def __init__(self, name):
        self.name=name # Define an attribute

    # Define a method
    def study(self):
        print(self.name, "is studying")
 
student1 = Student("John")
print(type(student1))

student1.study()
print(student1.name)

student2= Student("Mary")
student2.study()
print(student2.name)