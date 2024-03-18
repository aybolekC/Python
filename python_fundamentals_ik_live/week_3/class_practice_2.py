class Dog:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        print("Created a new dog object named ", name)

    def walk(self):
        print("I am walking", self.name)

    def weigh(self):
        print(self.name + "'s weight is " + str(self.weight))

    def __repr__(self):
        return "(Name:" + self.name + ", Age: " + str(self.age) + ", Weight: " +str(self.weight) +")"


dog1= Dog("Sky", 6, 5)
dog1.walk()
dog1.weigh()
print(dog1)





