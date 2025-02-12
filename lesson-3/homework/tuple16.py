# Determine if the tuple is sorted in ascending order and return a boolean.

tuple1=(1,2,3,4,5,6,7,8,9,10)
tuple2=(1,2,3,4,5,6,7,8,9,10,5)

print(True if tuple1 == tuple(sorted(tuple1)) else False)
print(True if tuple2 == tuple(sorted(tuple2)) else False)