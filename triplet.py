#Task-6- Question-9-Find triplet number
lists = [10, 20, 30, 9]
sum = 0
add = 0
m = 0
newLists = []
for list in lists:
    l = list
    sum = sum + l
#print(sum)

for j in range(0, 4):
    for i in range(m, 4):
        newLists.append(lists[i])
        add = add + lists[i]
    print(newLists)   
    print (add)
    
    if (add == 59):
        print("Triplet")
    print("\n")
    add = 0
    m = m+1
    newLists = []
