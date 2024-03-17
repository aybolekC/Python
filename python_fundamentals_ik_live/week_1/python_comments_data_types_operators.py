#======================Comments===============================
# This is my first lin eof comments with a single- line comment.

"""
This is my multi-line comment with actually more than 
one line in this example.
"""
print("Hello world!")

#===============================Data types=============================
a=10
b=6.2
c="mu first string"
d= True
print(a,b,c,d)

#example 2
a=10
print(type(a))
a=6.2
print(type(a))
a="Hey there"
print(type(a))
a=True
print(type(a))

#===============operators===========================================
x=10
y=3
#arithmetic operators
print("x + y = ", x + y)
print("x - y = ", x - y)
#comparison operators
print("x == y ? ", x==y)
print("x<y ? ", x<y)

#Example 2
x=10
y=20
name="Alice"
#logical operators
print("x > 0 and y > 0:  ", x>0 and y>0)
print("not x<0: ", not x<0)
#other operators
print("'A' in name: ", 'A'in name)
print("x is y:  ", x is y)

#===================Comparison =========================
a=5
b=5
print(a==b) #compare the value
print(a is b)
a=5
b=5.0
print(a==b) #compare the value
print(a is b) #compare the value and data type

#==============logical operatiions=======================

a=True
b=False
print(a and b)
print(a or b)
print(not a)