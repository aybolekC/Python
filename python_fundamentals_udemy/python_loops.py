
#======Print 1 to 10 using while loop===================
print("Print 1 to 10 using while loop")
number=1

while number<=10:
    print(number)
    number=number+1

#=================for loop=============================
print("Print 1 to 10 using for loop and range")

for i in range(10):
    print(i)
    
print("Print number in given range using for loop and range")
for i in range(3,7):
    print(i)    
    
print("Print number in given range incrementing by 2 using for loop and range")
for i in range(3,9,2):
    print(i) 

print("Print list elements using for loop")

fruit=['apple','pear','grapes','melon','orange']
for f in fruit:
    print(f)  
