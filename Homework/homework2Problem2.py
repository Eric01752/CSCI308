#Eric Schmidt
#Homework 2: Problem 2

#Get input from user
numRows = int(input("Enter number of rows: "))

#Create pattern
for x in range(1, numRows + 1):
    print("#", end="")
    for y in range(1, x):
        print(" ", end="")
    print("#")
