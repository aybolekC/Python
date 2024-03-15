
str1="Hello. I have a cat."
print(str1)

print(type(str1))

str2="She is a short hair"
print(len(str2))
print(str1+" "+str2)


str3="__".join([str1, str2])
print(str3)
print(len(str3))

print(str1[0])
print(str1[0:5])
print(str1[7:])
print(str1[:7])
print(str1[:])

hi=str1[0:5]
print(hi)
print(hi.upper())

str1a=str1[:] #copy a string
print(str1a)
print(str1a.split())

print(str1a.replace('cat', 'black cat'))