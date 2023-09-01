#Task-6 - Question -8 -Find minimum element in list
#lists = [10, 100, 40, 9, 8]

myNumber = int(input("Please enter the how many elements need in the list: "))
lists = []

for j in range(0, myNumber):
    num = int(input("Please enter your element: "))
    lists.append(num)
print(" The list is:", "=", lists)
    
minElement = lists[0]
#for i in range(0, myNumber):
#    if (lists[i] < minElement):
#        minElement = lists[i]
#print(minElement)

for list in lists:
    if (list < minElement):
        minElement = list
print(minElement)
    

        