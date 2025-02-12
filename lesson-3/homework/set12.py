#Given a set and an element, add the element to the set if it is not already present.

set1={1,2,3,4,5}
element=6

if element not in set1:
    set1.add(element)
print(set1)
