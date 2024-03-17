

# a=[4, 2, 2, 3, 1]
# b=[2, 2, 2, 3, 3]


a=[6,2,4]
b=[1,5,3,7]
result=[]

for item in a:
    if item in b:
        result.append(item)
        b.remove(item)

print(result)       