#Given a dictionary and a key, retrieve the associated value, considering what to return if the key doesn’t exist.

dict1 = {'a': 1, 'b': 2, 'c': 3}
key = 'b'
print(dict1.get(key, 'Key not found'))

