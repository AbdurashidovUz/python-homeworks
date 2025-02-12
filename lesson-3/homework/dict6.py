#Given two dictionaries, create a new dictionary that combines both.

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)