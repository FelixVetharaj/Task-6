#Task-6-Question-2-Find prime number in the list and count
lists = [10, 501, 22, 37, 100, 999, 87, 351]
notPrimeNumberLists = []
noDups =[]
for list in lists:
   for i in range (2, 10):
      if (list % i == 0 ):
         notPrimeNumberLists.append(list)

#print(notPrimeNumberLists) # find out not prime numbers in the list
#lists1 = (set(notPrimeNumberLists)&set(lists))
#print(lists1)

for lists1 in notPrimeNumberLists:
   if lists1 not in noDups:
      noDups.append(lists1)
#print("Not prime numbers in the list:",noDups) # remove duplicates from the not prime number list

#compare not prime number list and lists remove common element and print prime number
for i in lists[:]:
   if i in noDups:
      lists.remove(i)
print("The prime number in the list is:",lists)
l =len(lists)
print("The count of prime number is:",l)

   


      
    


         



