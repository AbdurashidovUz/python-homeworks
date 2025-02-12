#Given two lists, create a new set that merges both lists and removes duplicates.
list1=[1,1,2,2,3,3,4,4,5]
list2=[2,2,3,3,4,4,5,6]

set1=set(list1+list2)
print(set1)
