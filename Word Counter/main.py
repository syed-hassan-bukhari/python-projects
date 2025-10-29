import os

def count_words(file_path):
    try:
        
        file_path = os.path.expanduser(file_path)

        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
            words = text.split()
            print(f"\n✅ Total words in '{file_path}': {len(words)}")
    except FileNotFoundError:
        print("\n File not found. Please check the path and try again.")
    except Exception as e:
        print(f"\n An error occurred: {e}")

file_path = input("Enter full file path (e.g. C:/Users/Hassan/Desktop/demo.txt): ").strip()
count_words(file_path)
