#From a given tuple, find the second largest element.
#Find Second Smallest: From a given tuple, find the second smallest element.

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,1,1,1,1)
sorted_tuple = tuple(sorted((set(t))))
print("Second largest element is:", sorted_tuple[-2])
print("Second smallest element is:", sorted_tuple[1])
