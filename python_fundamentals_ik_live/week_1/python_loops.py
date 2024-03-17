for i in range(5): #
    print("This is iteration :", i)
    
counter=0
while counter<5:
    print("this is iteration: ", counter)
    counter+=1 # counter=counter+1
    
#==================nested====================
for i in range(5): 
    if i==3:
        print("This is iteration :", i)

#===================================================
for i in range(5):
    for j in range(10):
        print(i*j)

#===================break ===============================
for i in range(5): 
    print("This is iteration ", i)
    if i==3:
        break
#===================continue will skip any line of code coming after it ===============================

#this will print all iterations
for i in range(5): 
    print("This is iteration ", i)
    if i==3:
        continue
# this will skip printing when i is equal to 3
for i in range(5): 
    if i==3:
        continue
        print("Something please")
    print("This is iteration ", i)

#========================nested loop break======================================
for i in range(5):
    for j in range(5):
        if i==1:
            break
        print("This is iteration: ", i , j)

#=======================continue with nested loop==========================

for i in range(5):
    for j in range(5):
        if i==3:
            continue
            print("Something please")
        print("This is iteration: ", i , j)

    
    






