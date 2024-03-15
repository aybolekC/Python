try:
    num=float(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid number. ")

#========================input and data type=======================

age=input("Please can you provide your age: ")

print(age)
print(int(age)) 
#comparing value with int
# NaN, None, random or error    

#=====================================================================

#Collect user input
name=input("Enter your name: ")
age=input("Enter your age: ")

#Type casting for age
age=int(age)

print("Hello, " + name + "! You are " + str(age) + " years old.")


#===========================type casting ========================================
a=10
b=20
c=True
d=False
e="Hello"


print(str(a))
print(str(c))

#converting bool to int
print(int(c))
print(int(d))

k=4.55
print(int(k))
k=4.99
print(int(k))

k=4.9999999999999999
print(int(k))

k=4.7777777777777777
print(int(k))


#Comparing boolean 
print(bool(0))
print(bool(1))

#everything non 0 will be true for bool 
print(bool(1989873456787663))
print(bool(-1989873456787663))

#=========================================================

a=1000
print(a is 1000)
print(id(a))
print(id(1000))
