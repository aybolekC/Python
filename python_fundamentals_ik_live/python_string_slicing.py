
numbers=[1,2,3,4,5,6,7,8,9,10]

slice_negative=numbers[-5:-2]

print("Negative index slice: ", slice_negative)

#OUTPUT: [6,7,8]
#============================more examples===================================

l=[1,2,3,4,5,6,7,8,9,10]

print(l[2:6])

#third number represents skip pattern second print will jump 2 ahead each time
print("result for l[2:6:1]")
print(l[2:6:1])
print("result for l[2:6:2]")
print(l[2:6:2])
print("result for l[-5:-2]")
print(l[-5:-2])
print("result for l[5:-2]")
print(l[5:-2])
print("result for l[4:-2]")
print(l[4:-2])
print("result for l[4:-8]")
print(l[4:-8])

print("result for l[::-1]")
print(l[::-1])

print("l.reverse()")
l.reverse()
print(l)