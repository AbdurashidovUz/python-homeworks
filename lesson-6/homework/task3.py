import os
import string
from collections import Counter


def create_sample_file():
    print("sample.txt not found. Please enter a paragraph to create the file:")
    text = input("Enter text: ")
    with open("sample.txt", "w") as file:
        file.write(text)


def read_file():
    if not os.path.exists("sample.txt"):
        create_sample_file()
    with open("sample.txt", "r") as file:
        return file.read()


def count_word_frequency(text):
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return Counter(words)


def save_report(total_words, common_words):
    with open("word_count_report.txt", "w") as file:
        file.write("Word Count Report\n")
        file.write(f"Total Words: {total_words}\n")
        file.write("Top 5 Words:\n")
        for word, count in common_words:
            file.write(f"{word} - {count}\n")


def main():
    text = read_file()
    word_counts = count_word_frequency(text)
    total_words = sum(word_counts.values())
    common_words = word_counts.most_common(5)

    print(f"Total words: {total_words}")
    print("Top 5 most common words:")
    for word, count in common_words:
        print(f"{word} - {count} times")

    save_report(total_words, common_words)



if __name__ == "__main__":
    main()
