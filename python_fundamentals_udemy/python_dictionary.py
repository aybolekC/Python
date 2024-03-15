dict={'Japan':'Tokyo', 'China':'Beijing',
    'South Korea':'Seul', 'North Korea':'Pyongyong', 'a':3}


print(dict)

print(len(dict))

print(dict.keys())
print(dict.values())

dict2=dict.copy()
print("=====================Copy====================")
print(dict2)

print("=====================deleting ====================")
del dict2['a']
print(dict2)
print(dict)

print("=====================adding ====================")
dict2["Hk Sar"]="Hong Kong"
print(dict2)
dict2[10]="bullseye"
print(dict2)

print("============printing value of the key=================")
print(dict2["China"])
print(dict2[10])

print("=======check if the pair is available in dictionary======")
print('b' not in dict)
print('a' not in dict)

print('b' in dict)
print('a' in dict)

print("============sorting dictionary=================")
print(sorted(dict))