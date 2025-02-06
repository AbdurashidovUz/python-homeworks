a=input('Enter a string: ')
vowels = 'euioa'
a.lower()
vowels_count=0
consonants_count=0

for char in a:
    if char.isalpha():
        if char in vowels:
            vowels_count+=1
        else:
            consonants_count+=1

print(vowels_count, consonants_count)
