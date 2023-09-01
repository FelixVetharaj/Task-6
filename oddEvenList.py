# Task-6 - Question 1- Create two list which have all the Even numbers and another list which have odd numbers
lists = [10, 501, 22, 37, 100, 999, 87, 351]
evenNumberLists = []
oddNumberLists = []
for list in lists:
    if (list % 2 == 0):
        evenNumberLists.append(list)
    else:
        oddNumberLists.append(list)
print("Even Number List", "=", evenNumberLists)
print("Odd Number List", "=", oddNumberLists)
