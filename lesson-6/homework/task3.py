def create_sample_file():
    print("Please enter a paragraph to create the file:")
    text = input("Enter text: ")
    with open("sample.txt", "w") as file:
        file.write(text)

def read_file():
    try:
        with open("sample.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        create_sample_file()

def count_word_frequency(text):
    text = text.lower().replace(",", "").replace(".", "")
    words = text.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def save_report(total_words, common_words):
    with open("word_count_report.txt", "w") as file:
        file.write(f"Total words: {total_words}\n")
        file.write("Top 5 most common words:\n")
        for word, count in common_words:
            file.write(f"{word} - {count} times\n")

def main():
    text = read_file()
    word_counts = count_word_frequency(text)
    total_words = sum(word_counts.values())
    common_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:5]

    print(f"Total words: {total_words}")
    print("Top 5 most common words:")
    for word, count in common_words:
        print(f"{word} - {count} times")

    save_report(total_words, common_words)

if __name__ == "__main__":
    main()
