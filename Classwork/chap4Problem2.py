total = 0
while True:
    number = int(input("Enter a positive number(-1 to quit): "))
    if number == -1:
        break
    else:
        total += number
print("Sum of all numbers entered: " + str(total))
