# Task 6 - Question 7 - Print the fisrt non repeating element in the list
lists = [100, 10, 20, 10, 100, 30]

# Find duplicate in the list
noDuplicates = []
duplicates = []

for list in lists:
    if list not in noDuplicates:
        noDuplicates.append(list)
    else:
        duplicates.append(list)
print(noDuplicates)
print(duplicates)

# Compare the duplicates and list and remove duplicate elements
noDups = []

for i in lists:
    if i not in duplicates:
        noDups.append(i)
# Print the first non repeating element in the list
print(noDups)
print(noDups[0])