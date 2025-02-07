s = input("Enter a string: ")

if any(char.isdigit() for char in s):
    print("The string contains at least one digit")
else:
    print("The string does not contain any digits")
