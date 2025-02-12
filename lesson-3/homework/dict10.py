#Given a dictionary and a key, retrieve the key-value pair if the key exists.

dict1 = {'a': 1, 'b': 2, 'c': 3}
key = 'b'

if key in dict1:
    print(key, dict1[key])
else:
    print('Key not found')