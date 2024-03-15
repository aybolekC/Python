mfood=['egs', 'coffee', 'apple', 'cheese cube']
print(mfood)

nums=[4, 56, 11, 7, 15]
print(nums)

mix=[5, 11, 76,'cat', 'dog', 'rat']
print(mix)

mix2=[12, 2, 'eggs', 32, 'coffee', nums]
print(mix2)


contact=[]  #empty list

contact.append("Gary")
contact.append("Mary")

print(contact)
#add several items into a list

contact.extend(['Ray','Tia', 3,8,2])
print(contact)

#insert
contact.insert(2, "Molly")
print(contact)


nums2=[2,7,14,5,26,19,30,35]
print(nums2)

nums2.remove(14)
print(nums2)

del nums2[3]
print(nums2)

removedNumber=nums2.pop(2)
print(removedNumber)
print(nums2)

nums2[1]=90
print(nums2)