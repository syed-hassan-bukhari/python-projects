import time
import random

def typing_speed_test():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a powerful and versatile programming language.",
        "Typing fast requires focus and practice.",
        "Artificial intelligence is changing the world.",
        "Consistency is the key to mastering any skill."
    ]

    
    sentence = random.choice(sentences)
    print("\n⌨ Typing Speed Test")
    print("Type this sentence:\n")
    print(sentence)
    print("\nStart typing below:")

    
    start_time = time.time()
    typed = input("\nYour input: ")
    end_time = time.time()

    
    time_taken = end_time - start_time
    words = len(typed.split())
    wpm = (words / time_taken) * 60  

    
    correct_chars = 0
    for i in range(min(len(sentence), len(typed))):
        if sentence[i] == typed[i]:
            correct_chars += 1
    accuracy = (correct_chars / len(sentence)) * 100

    
    print("\n⏳ Results:")
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Typing Speed: {wpm:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    typing_speed_test()
