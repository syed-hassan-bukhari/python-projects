📝 Unique Word Extractor
📌 Description

This Python script reads a text file and extracts unique words (words that appear only once). It ignores letter case (treats “Great” and “great” as the same word) and displays the unique words in sorted order.

⚙️ How It Works

The program reads the contents of a text file (TXT_file.txt).

It uses regular expressions (re module) to extract words.

It counts the occurrences of each word using a dictionary.

Words that appear only once are stored and displayed in alphabetical order.

▶️ How to Run

Make sure you have a text file named TXT_file.txt in the same folder as the script.

Run the Python file:

python main.py