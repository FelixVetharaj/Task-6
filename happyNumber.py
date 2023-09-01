# Task-6- Question 3-Find out how many happy numbers in the list and which are in the list
lists = [10, 501, 22, 37, 100, 999, 87, 351]
happyNumbers = []
for list in lists:
    lastDigit = list % 10  # % 10 remainder gives the last digit
    #print (lastDigit) 
    digit = list // 10    # // 10 Quotient gives the remaining digits in the number
    #print("Remaining Digit: ", digit)

    middleDigit = digit % 10
    #print(middleDigit)
    digit1 = digit // 10
    #print("Remaining Digit: ", digit1)

    firstDigit = digit1 % 10
    #print(firstDigit)
    digit2 = digit1 // 10
    #print("Remaining Digit: ", digit2)

    happyNumber = lastDigit ** 2 + middleDigit ** 2 + firstDigit ** 2
    #print(happyNumber)

    if (happyNumber == 1):
        happyNumbers.append(list)
print("Happy Number List ", "=",  happyNumbers)
print("The number of happy numbers in the list: ", len(happyNumbers))





