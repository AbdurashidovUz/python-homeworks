#Access the first element of a tuple, considering what to return if the tuple is empty.

tuple1 = (1, 2, 3, 4, 5)
print(tuple1[0] if tuple1 else "Empty tuple")
tuple2 = ()
print(tuple2[0] if tuple2 else "Empty tuple")