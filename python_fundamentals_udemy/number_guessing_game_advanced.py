# computer to generate numbers in given range
#input my guess
import random

computer_number=random.randint(1,20) # store the random numbers generated using random

print(computer_number)

def same_number(target, number):
    if target == number:
        result = "Win"

    elif target>number: # computer number > than my guess
        result = "Low"
    else:
        result="High"

    return result


print("Lets guess a number")

guess=int(input("What is your guess?"))

high_or_low = same_number(computer_number, guess)

while high_or_low != "Win":
    if high_or_low == "Low":
        guess=int(input("Too low. Try again"))
    else:
        guess=int(input("Too high. Try again"))

    high_or_low = same_number(computer_number, guess)

input("Exit")