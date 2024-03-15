import random
x = 4

if x > 6:
    print("big")
else:
    print("small")

#======================================================

ans1="cat"
ans2="dog"
ans3="goat"
ans4="tortoise"
ans5="kitten"

print("select my pet")

#ques=input("Which is the most suitable pet for keeping in a flat?\n")

print("Which is the most suitable pet for keeping in a flat?")
choice=random.randint(1,5)

print(choice)

if choice==1:
    answer=ans1
elif choice==2:
    answer=ans2
elif choice==3:
    answer=ans3
elif choice==4:
    answer=ans4
else: 
    answer=ans5


print(answer)    