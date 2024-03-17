"""
Qestion:
Suppose you want to find the first pair of divisors for a given number within a specific range.

Hint:
You can use nested loops to iterate through the possibilities, 
and break statement to exit the loop once the pair is found
"""

"""
my solution: did not work 

num=10
i=2
counter=0
for i in range(num):
    while counter!=2:
        if(num//i==0):
            counter+=1
"""

#Solution
number = 64
found_divisor= False

for i in range(2, number):
    if found_divisor: # If the divisor is found, break the outer loop
        break
    for j in range(2, number):
        if i*j==number:
            print("The first pair of divisors for " + str(number) + " are " + str(i) +" and " + str(j))
            found_divisor=True # Set the flag to the true
            break # Break out of the inner loop
#OUTPUT:
#The first pair of divisors for 64 are 2 and 32