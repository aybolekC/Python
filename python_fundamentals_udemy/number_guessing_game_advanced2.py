# computer to generate numbers in given range
#input my guess
import random

computer_number=random.randint(1,20) # store the random numbers generated using random

print(computer_number)

guessesTaken = 0

score=5

while guessesTaken < 5:
    guess=int(input("What is your guess?"))
    
    guessesTaken=guessesTaken+1

    if guess==computer_number:
        score=5-guessesTaken
        s=str(score)

        print('You win with score of ' + s)
    
    elif guess>computer_number:
        print("Your guess is too high")
    else: 
        print("Your guess is too low")


if guess==computer_number:
    print("Done")
else:
    print("You lose. The computer guessed number is " + str(computer_number))
