#Given a tuple, find the maximum element of a specified subtuple.

tuple1=(1,2,3,4,5,6,7,8,9,10)
print("Original tuple:")
print(tuple1)
slice1=tuple1[3:8]
print("\nSliced tuple:")
print(slice1)
print("\nMaximum element of the sliced tuple:")
print(max(slice1))
