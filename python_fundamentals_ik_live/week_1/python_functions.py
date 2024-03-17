#Function definition
def greet(name):
    message="Hello, " + name + "!"
    return message

#Function call
greeting=greet("Aya")
print(greeting)

#===============================function 2===============================
#Function definition
def greet2(name):
    message="Hello, " + name + "!"
    print(message)


#Function call
greeting=greet2("Aya")
print(greeting)

#===============================function 3===============================
#Function definition
def greet3(name):
    message="Hello, " + name + "!"
    print(message)
    return


#Function call
greeting=greet3("Aya")
print(greeting)

#=============================================================================

def first_funct(a,b,c):
    print(a*b*c)
first_funct(2,3,2)   

#having default value for c
def first_funct2(a,b,c=2):
    print(a*b*c)
first_funct2(2,3)   

#having default value for c and b
def first_funct3(a,b=2,c=2):
    print(a*b*c)
first_funct3(2)   

#default value should be initialized at the end of parameter list otherwise will fail to compile
#below examples will fail 
"""
def first_funct4(a,b=2,c):
    print(a*b*c)
first_funct4(2,3)   

def first_funct5(a,d,b=2,z=4,c):
    print(a*b*c)
first_funct5(2,3) 
"""

#we can override defatul value
#having default value for c and b
def first_funct6(a,b=2,c=2):
    print(a*b*c)
first_funct6(2,3,4)  

#=========================more examples==============================
def power(base, exponent=2):
    return base**exponent

print(power(3))   

print(power(3,3)) 

#python never doing type check in function definition 
# you will need to install mypy for actual type checking 
def func1(x: int)->int:
    return x


#above function will work for all data types since python not doing type check
func1(5)
func1(5.2)
func1("Hello")
func1(True)


