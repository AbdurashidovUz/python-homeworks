words = input("Enter words separated by spaces: ").split()
separator = input("Enter a separator (e.g., -, ,): ")

result = separator.join(words)
print("Joined string:", result)
