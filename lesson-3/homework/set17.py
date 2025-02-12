#Given a set of integers, create a new set that contains only the odd numbers.

set1={1,2,3,4,5,6,7,8,9,10}
set2=set()
for i in set1:
    if i%2!=0:
        set2.add(i)
print(set2)