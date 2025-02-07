a = input("Enter a string: ")
b = input("Enter a symbol: ")

vowels = "AEIOUaeiou"
result = "".join(b if char in vowels else char for char in a)

print(result)
