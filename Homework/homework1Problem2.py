#Eric Schmidt
#Homework 1: Problem 2

#Get input from the user
print("BMI Calculator")
weight = int(input("Enter your weight(pounds): "))
height = int(input("Enter your height(inches): "))

#Calculate the BMI
BMI = weight * 703 // height**2

#Display the BMI and status
print("Your BMI is " + str(BMI))
if BMI >= 18.5 and BMI <= 25:
    print("You have an optimal weight.")
elif BMI < 18.5:
    print("You are underweight.")
else:
    print("You are overweight.")
