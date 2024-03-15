# computer to generate numbers in given range
#input my guess
import random

computer_number=random.randint(1,4) # store the random numbers generated using random

def same_number(target, number):
    if target==number:
        result="Win"

    else:
        result="Fail"
    return result


print("Lets guess a number")

guess=int(input("What is your guess?"))

print(same_number(computer_number, guess))