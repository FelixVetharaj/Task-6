# Task-6-Question 6- Find duplicate in below list individually and also all the three list

lists = [ 22, 11, 33, 22, 11, 55]
lists1 =[100, 75, 86, 75, 22, 55]
lists3 =[22, 10, 80, 90, 44, 10]

print(" List 1:",  "=",  lists)
print(" List 2:",  "=", lists1)
print(" List 3:",  "=", lists3)


# Find duplicate of first list
duplicates = []
noDuplicates = []

for list in lists:
    if list not in noDuplicates:
        noDuplicates.append(list)
    else:
        duplicates.append(list)
print("The duplicates in the first list: ", duplicates)
#print(noDuplicates)

# Find duplicate of second list
duplicates1 = []
noDuplicates1 = []

for list1 in lists1:
    if list1 not in noDuplicates1:
        noDuplicates1.append(list1)
    else:
        duplicates1.append(list1)
print("The duplicates in the second list: ", duplicates1)

#Find duplicate of third list
duplicates2 = []
noDuplicates2 = []

for list2 in lists3:
    if list2 not in noDuplicates2:
        noDuplicates2.append(list2)
    else:
        duplicates2.append(list2)
print("The duplicates in the third list: ", duplicates2)

# Find duplicate of all 3 lists.

#c = set(lists) & set(lists1) & set(lists3) #simple form to find duplicate 
#print(c)

d = []  # Find duplicates comparing lists and lists1
for i in lists:
    if i in lists1:
        d.append(i)
#print(d)

d1 = [] # Find duplicates comparing d and lists3
for j in d:
    if j in lists3:
        d1.append(j)
#print(d1)

d3 = []  # Remove any duplicates in d1 and add to d3
for k in d1:
    if k not in d3:
        d3.append(k)
print("The duplicate of all the three list is: ", d3)
