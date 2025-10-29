import random 

while True:
    roll = random.randint(1,6)
    print(f" you rolled : {roll}")

    again=input("roll again? (Y/N): ").lower
    if again == "n":
        print(" thanks for rolling")
        break
    