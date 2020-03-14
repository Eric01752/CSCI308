#Eric Schmidt
#Homework 4: Problem 1

#Fills list with the numbers 2 to the input number
#Return: list
def populateList(number):
    numList = []

    for x in range(2,number + 1):
        numList.append(x)
    return numList

#Checks to see if all numbers from 2 to input number are prime
#Prints the number if it is prime
def checkIfPrime(checkNumber):
    for x in range(2, checkNumber):
        if checkNumber % x == 0:
            break
    else:
        print(checkNumber, " is a prime number")

#Gets input from the user
#Calls the populateList and CheckIfPrime functions
def main():
    number = int(input("Enter a number greater than 1: "))

    numList = populateList(number)

    for x in numList:
        checkIfPrime(x)

main()
