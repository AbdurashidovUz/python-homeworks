#First Element: Access the first element of a list, considering what to return if the list is empty.
#Last Element: Access the last element of a list, considering what to return if the list is empty.

def first_element(list):
    if len(list) == 0:
        return None
    else:
        return list[0]

def last_element(list):
    if len(list) == 0:
        return None
    else:
        return list[-1]

# Test Cases
print(first_element([1, 2, 3])) # 1
print(first_element([])) # None
print(last_element([1, 2, 3])) # 3
print(last_element([])) # None