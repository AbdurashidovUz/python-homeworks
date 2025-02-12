#Given a tuple and an element, find all the indices of that element in the tuple.

tuple1=(1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9)
element=1
index=0
for i in tuple1:
    if i==element:
        print(index)
    index+=1

