# Return uncommon elements of lists. Order of elements does not matter.

list1=[]
list2=[]
print("Enter 3 elements for list1:")
for i in range(3):
    list1.append(int(input()))
print("Enter 3 elements for list2:")
for i in range(3):
    list2.append(int(input()))
list3=list1+list2
for i in list1:
    for j in list2:
        if i==j:
            list3.remove(i)
            list3.remove(j)

print(list3)

