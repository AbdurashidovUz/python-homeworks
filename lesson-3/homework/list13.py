# Given a list and an element, find the index of the first occurrence of the element.
# If the element is not in the list, return -1.

list2=[1,2,3,4,5,6,7,8,9,10]
element=5

if element in list2:
    print(list2.index(element))
else:
    print(-1)