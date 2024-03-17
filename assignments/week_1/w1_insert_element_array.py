
print("======================Solution with built in methods insert(), pop()")
nums=[2,4,5,6,-1]
def insert_element_at_position(nums, element, position):
    nums.insert(position-1, element)
    nums.pop(len(nums)-1)
    return nums

print(insert_element_at_position(nums,3,2))


print("======================Solution from trainer===============================")
nums=[2,4,5,6,-1]
def insert_element_at_position2(nums, element, position):
    for i in range(len(nums)-1, position-1, -1):
        nums[i]=nums[i-1]
    nums[position-1]=element
    return nums

print(insert_element_at_position2(nums,3,2))    
    
