#===========================reverse array with slicing ===================================
nums=[17,66,78,35,50] 
print("=======================Solution with slicing solution===================================")
#output of slicing solution will return new array, which will fail requirement
def reverse_array_slicing(nums):
    print(nums)
    return nums[::-1]

print(reverse_array_slicing(nums))

#===========================reverse array with reverse method ===================================
print("=======================Solution with reverse method====================================")
print(nums)
def reverse_array_reverse_method(nums):
    #print(nums)
    nums.reverse()
    return nums

print(reverse_array_reverse_method(nums))

#===============================================================================
nums2=[17,66,78,35,50] 

print("=======================Solution by looping through====================================")
print(nums2)
def reverse_array_looping_through(nums2):
    n=len(nums)
    for i in range(n-1):
        print(nums[(n-1)-i], end=' ')
        i=i+1

print(reverse_array_looping_through(nums2))        

#===============================================================================

print("=======================2 pointer solution with while loop====================================")
print(nums2)
def reverse_array_two_pointer_while_loop(nums2):
    start=0
    end=len(nums2)-1
    while start<end:
        nums2[start], nums2[end]=nums2[end], nums2[start]
        start+=1
        end-=1
    return nums2      
    
   
print(reverse_array_two_pointer_while_loop(nums2))      