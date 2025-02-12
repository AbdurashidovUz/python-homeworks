#Given a dictionary, count how many times a specific value appears across the keys.
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 1, 'f': 3, 'g': 2}
value = 2
count = 0
for key in dict1:
    if dict1[key] == value:
        count += 1
print(count)