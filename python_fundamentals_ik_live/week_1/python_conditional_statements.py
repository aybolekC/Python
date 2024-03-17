#==================Example 1================================
age=18
if age>=18:
    print("You are eligible to vote. ")
else:
    print("You are not eligible to vote. ")

#==================Example 1================================

age=19
if age>=18:
    print("You are eligible to vote. ")
elif age>=18 and age<=25:
    print("You are eligible to vote and it id not your first time voting ")
else:
    print("You are not eligible to vote. ")
    
print("This is outside of the if-else block")

#========================================================================

age=25
if age>=18 and age<=25:
    print("You are eligible to vote and it id not your first time voting ")
elif age>=18: 
    print("You are eligible to vote. ")
else:
    print("You are not eligible to vote. ")
    
print("This is outside of the if-else block")

#=====================================================================

age=26
if age>=18 and age<=25:
    print("You are eligible to vote and it id not your first time voting ")
elif age>=18: 
    print("You are eligible to vote. ")
else:
    print("You are not eligible to vote. ")
    
print("This is outside of the if-else block")

#======================================================================

age=16
if age>=18 and age<=25:
    print("You are eligible to vote and it id not your first time voting ")
elif age>=18: 
    print("You are eligible to vote. ")
else:
    print("You are not eligible to vote. ")
    
print("This is outside of the if-else block")

#=========================nested if-else block=============================================================

age=19
if age>=18:
    print("You are eligible to vote")
    if age<=40:
        print("you have experience voting")
    else:
        print("you are really experienced on voting")
elif age>=18 and age<=25: 
    print("You are eligible to vote and it id not your first time voting ")
else:
    print("You are not eligible to vote. ")
    
print("This is outside of the if-else block")

#====================================using logical operators===================================
age=25
has_license=True

if age>=18 and has_license:
    print("You are allowed to drive")
elif age>=18 and not has_license: 
    print("You need a license to drive")
else:
    print("You are old enough to drive. ")

#=================================================================================    


