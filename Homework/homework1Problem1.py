#Eric Schmidt
#Homework 1: Problem 1

#Coin values
PENNY = 1
NICKEL = 5
DIME = 10
QUARTER = 25

#Get input from the user
print("Try to make exactly one dollar using pennies, nickels, dimes, and quarters.")
numPennies = int(input("Enter the number of pennies: "))
numNickels = int(input("Enter the number of nickels: "))
numDimes = int(input("Enter the number of dimes: "))
numQuarters = int(input("Enter the number of quarters: "))

#Get coin value times the number of each coin given
numPennies *= PENNY
numNickels *= NICKEL
numDimes *= DIME
numQuarters *= QUARTER

#Add all coin amounts to get total
totalAmount = numPennies + numNickels + numDimes + numQuarters

#Check to see if total is equal to one dollar
if totalAmount == 100:
    print("You made exactly one dollar. You win!")
elif totalAmount > 100:
    print("You went over one dollar. You lose.")
else:
    print("You were under one dollar. You lose.")
