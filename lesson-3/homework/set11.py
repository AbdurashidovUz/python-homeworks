#Given two sets, create a new set that contains elements that are in either set but not in both

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set3 = set1.symmetric_difference(set2)
print(set3)