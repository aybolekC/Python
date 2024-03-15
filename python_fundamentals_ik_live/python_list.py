fruits=["apple","banana", "cherry"]
print(fruits)
print(fruits[0])

print(fruits[1:3])

fruits[0]="grape"
print(fruits)
#================================list example==================================
my_first_list=["apple",1,True,"banana",4.5,"apple"]
print(my_first_list[3])
print(my_first_list)

my_first_list.remove("apple")
print(my_first_list)

print(my_first_list[2:3])
#=============================iteration over the list==============================

even_list=[x for x in range(101) if x%2==0]
print(even_list)

l=[1,4,39,49,205,2548,291,10]
for item in l:
    print(item)
    
#enumeration
l=[1,4,39,49,205,2548,291,10]
for index, item in enumerate(l):
    print(index,item)
    
 #============================================================================   