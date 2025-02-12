#Given two sets, check if they have no elements in common.
set1={1,1,2,2,3,3,4,5,5,6}
set2={2,3,4,5,6}

for i in set1:
    for a in set2:
        if i==a:
            print(i)
