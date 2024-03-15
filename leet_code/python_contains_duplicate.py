"""
217 - Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array,
and return falseif every element is distinct.

"""
# my solution
nums=[1,2,3,1]
nums2=[1,2,3,4]
nums3=[1,1,1,3,3,4,3,2,4,2]

print("My solution")
def duplicate(nums):
    result=False
    for i in range(0, len(nums)):
       # print(nums[i])
        for j in range(1, len(nums)):
            if(nums[i]==nums[j]):
                result=True
                
        return result

print(duplicate(nums))    
print(duplicate(nums2))
print(duplicate(nums3)) 

#=====================Trainers solution========================================

#Solution #1

print("Trainer solution - 1")
#def containsDuplicate(self, nums: List[int])->bool:
def containsDuplicate2(nums):
    n=len(nums)
    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i]==nums[j]:
                return True
    return False
    
print(containsDuplicate2(nums))   
print(containsDuplicate2(nums2))
print(containsDuplicate2(nums3))

# Solution #2
print("Trainer solution - 2")
#def containsDuplicate(self, nums: List[int])->bool:
def containsDuplicate3(nums):
    nums.sort()
    n=len(nums)
    for i in range(1,n):
            if nums[i]==nums[i-1]:
                return True
    return False
    
print(containsDuplicate3(nums))   
print(containsDuplicate3(nums2))
print(containsDuplicate3(nums3))

# Solution #4
print("Trainer solution - 3")
def containsDuplicate4(nums):
    seen=set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
    
print(containsDuplicate4(nums))   
print(containsDuplicate4(nums2))
print(containsDuplicate4(nums3))

