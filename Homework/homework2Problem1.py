#Eric Schmidt
#Homework 2: Problem 1

#Get input from user
#Checks: input greater than 0
print("Calculating a factorial.")
while True:
    number = int(input("Enter a positive number: "))
    if number > 0:
        break
    else:
        print("Number was not positive.")

#Calculate factorial
factorial = 1
for x in range(1, number + 1):
    factorial = factorial * x

#Displays answer
print("The factorial of " + str(number) + " is " + str(factorial))
