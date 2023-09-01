# Task-6-Question -10- Sublist equal to zero
lists = [4,2,-3,1,6]
sum = 0
sum1 = 0
sum2 = 0
sublists = []
l=0
m =1
n=1

print("The list = ", lists)

length = len(lists)
print("The length of lists:", length)
print("\n")

# Index from 0 to 4
for j in range (0, length):
    for i in range(l, length):
         sublists.append(lists[i])
         sum = sum + lists[i]
    print(sublists)
    print(sum)
    if (sum2 == 0):
        print("The sublist sum is zero")
   
    print("\n")
    sum = 0
    l+=1
    sublists=[]
print("\n")

# Index from 1 to 4
for j in range (1, length):
    for i in range (m, length):
        sublists.append(lists[i])
        sum1 = sum1 + lists[i]
    print(sublists)
    print(sum1)
    if (sum2 == 0):
        print("The sublist sum is zero")

    print("\n")
    sum1 = 0
    m+=1
    sublists=[]
print("\n")

# Index from 1 to 3
for j in range (1, length-1):
    for i in range (n, length-1):
        sublists.append(lists[i])
        sum2 = sum2 + lists[i]
    print(sublists)
    print(sum2)
    
    if (sum2 == 0):
        print("The sublist sum is zero")
    print("\n")
    sum2 = 0
    n+=1
    sublists=[]