#Eric Schmidt
#Quiz 1: Problem 2

year = int(input("Enter a year: "))

if year % 100 == 0:
    if year % 400 == 0:
        print("February in the year " + str(year) + " has 29 days")
    else:
        print("February in the year " + str(year) + " has 28 days")
elif year % 100 != 0:
    if year % 4 == 0:
        print("February in the year " + str(year) + " has 29 days")
    else:
        print("February in the year " + str(year) + " has 28 days")
