
def get_pivot_index(numbers):
    for i in range(len(numbers)):
        left_sum=sum(numbers[0:i])
        right_sum=sum(numbers[i+1:len(numbers)])

        if(left_sum==right_sum):
            return i
    return -1


numbers=[2,3,1,-1,1,1,4]
print(get_pivot_index(numbers));  

numbers1=[2, 3, 5]
print(get_pivot_index(numbers1));  

 
numbers2=[0, 1, -1]
print(get_pivot_index(numbers2));  


