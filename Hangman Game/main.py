import random

def hangman():
    words = ["python", "hangman", "gemini", "buddy", "copy"]
    word = random.choice(words)  
    guessed = ["_"] * len(word)  
    attempts = 6 
    guessed_letters = set()

    print(" Welcome to Hangman!")
    print(" ".join(guessed))

    while attempts > 0:
        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
            print("Good guess!")
        else:
            attempts -= 1
            print(f" Wrong guess! Attempts left: {attempts}")

        print(" ".join(guessed))

        if "_" not in guessed:
            print(" Congratulations! You guessed the word!")
            break
    else:
        print(f" Game Over! The word was: {word}")


hangman()
