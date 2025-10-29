import random

user_score = 0
com_score = 0
tie = 0

while True:
    print("\nChoices are: \n1. Rock \n2. Paper \n3. Scissor")
    choice = int(input("Enter your choice from 1-3: "))
    while choice > 3 or choice < 1:
        choice = int(input("Enter a valid input (1-3): "))

    
    if choice == 1:
        user_choice = "rock"
    elif choice == 2:
        user_choice = "paper"
    else:
        user_choice = "scissor"
    print("You chose:", user_choice)

    
    computer = random.randint(1, 3)
    com_choice = ["rock", "paper", "scissor"][computer - 1]
    print("Computer chose:", com_choice)

    
    if ((user_choice == "paper" and com_choice == "rock") or
        (user_choice == "rock" and com_choice == "paper")):
        print("Paper wins")
        result = "paper"
    elif ((user_choice == "scissor" and com_choice == "rock") or
          (user_choice == "rock" and com_choice == "scissor")):
        print("Rock wins")
        result = "rock"
    elif user_choice == com_choice:
        print("It's a tie!")
        result = "tie"
    else:
        print("Scissor wins")
        result = "scissor"

    
    if result == "tie":
        tie += 1
    elif result == user_choice:
        print(" You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        com_score += 1

    
    print(f"Scores → You: {user_score} | Computer: {com_score} | Ties: {tie}")

    
    repeat = input("Do you want to play again? (Y/N): ")
    if repeat.lower() == "n":
        break
    

print("GAME OVER")
print(f"Final Score → You: {user_score}, Computer: {com_score}, Ties: {tie}")

