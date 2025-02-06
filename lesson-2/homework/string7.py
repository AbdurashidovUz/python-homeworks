a=input("Input a sentence: ")
b=input("Replace: ")
c=input("with: ")

if b in a:
    a=a.replace(b,c)
    print(a)
else:
    print("No given word is found")
