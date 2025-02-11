#Given a list and a sublist, check if the sublist exists within the list.

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sublist = [3, 4, 5]

result = str(sublist)[1:-1] in str(list1)[1:-1]

print(result)  
