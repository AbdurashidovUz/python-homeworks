#Given a tuple and an element, create a new tuple that removes the first occurrence of that element.

tuple1=(1,2,3,4,5,6,7,8,9,10)
element=5
tuple2=tuple1[:tuple1.index(element)]+tuple1[tuple1.index(element)+1:]
print(tuple2)
