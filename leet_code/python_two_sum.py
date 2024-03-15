"""
Two Sum 
* Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
* You may assume that each input would have exactly one solution, 
and you may not use the same element twice. 
* You can return the answer in any order.
"""
print("my solution")
#my solution
nums=[2,7,11,15]
target=9
solution=False

for i in range(len(nums)):
    if(solution):
        break
    #print(nums[i])
    for j in range(len(nums)):
        #print(nums[i], " ", nums[j])
        if(nums[i]+nums[j]==target):
            solution=True
            print("Solution is: " + str(i), " ", str(j))
            break


# trainer solution

""" 
type nums --> List[int]
type target----> int 
return type ---> List[int]
"""

print("trainer solution")

def twoSum(nums, target):
    # Iterate through the nums list up to the second last element
    for i in range(0, len(nums)):
        # Select the number at the current index
        num1=nums[i]
        
        # Iterate through the remaining numbers in the list
        for j in range(i+1, len(nums)):
            num2=nums[j]
            if num1+num2==target:
                return [i, j]

list1=[2,10,9,20,5,7]

result=twoSum(list1, 11)
print(result)

