
dict={'Japan':'Tokyo', 'China':'Beijing',
    'South Korea':'Seul', 'North Korea':'Pyongyong'}

print("By defatult for loop will print keys of the dictionary")
for i in dict:
    print(i)
print("Printing keys and values of the dictionary using for loop")
for k,v in dict.items():
    print(k, "capital city", v)

print("Pulling values by index using for loop")
for i in dict:
    print(i, dict[i])


print("arifmetic operations with for loop")
for i in range(21):
    if i % 2 == 0:
        print(i)