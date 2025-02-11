#Replace Element: Given a list, replace the first occurrence of a specified element with another element.

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
element=5
replace=10
index=list1.index(element)
list1[index]=replace
print(list1)