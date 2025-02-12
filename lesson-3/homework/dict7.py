# Given a dictionary and a key, remove the key if it exists, handling the case if it doesn’t.

dic1 = {'a': 1, 'b': 2, 'c': 3}
key = 'b'

if key in dic1:
    del dic1[key]
    print(dic1)
else:
    print(f'Key {key} does not exist in the dictionary')