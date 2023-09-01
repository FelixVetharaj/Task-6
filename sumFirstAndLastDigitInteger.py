# Task -6- Question 4- Sum of first and last digit integer
myNumber = int(input("Please enter your number: "))
myNumber = str(myNumber)
count = 0
add = 0
for digit in myNumber:
    length = len(digit)
    count = count + length
#print(count)

myNumber = int(myNumber)
for i in range(1, count+1):
    lastDigit = myNumber % 10  # % 10 remainder gives last digit
    print(lastDigit)
    remainingDigit = myNumber // 10   # // 10 Quotient gives remaining digits 
    #print(remainingDigit)
    myNumber = remainingDigit # New remaining digit

    if ( i == 1):
        #print (lastDigit)
        lDigit = lastDigit
    if (i == count):
        #print(lastDigit)
        fDigit = lastDigit
        add = lDigit + fDigit
print("The sum of first and last Digit: ", add)






