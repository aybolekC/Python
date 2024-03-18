
#=============MCQ4=======================================
class Employee:
    def __init__(self,id,age):
        self.id=id
        self.age=age
    
    def printID(self):
        print(self.id)
    
    def printAge(abc): # we can put name to replace self - self is not a keyword
        print(abc.age)


emp1=Employee('E001',30)
emp1.printAge()