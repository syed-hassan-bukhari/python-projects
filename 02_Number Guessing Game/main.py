import random

number = random.randint(1,100)
Guess=0

while Guess != number :
    Guess = int(input("Enter Guess: "))

    if ( Guess < number):
        print("Guess higher!: ")

    elif ( Guess > number):
        print("Guess lower!: ")
    else:
        print(" YOU WON ")
                