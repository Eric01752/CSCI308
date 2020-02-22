#Writes a series of numbers to a file
import random

numNumbers = int(input("Enter the amount of numbers to add to file: "))
write_Numbers = open("numbers.txt", "w")

for x in range(0, numNumbers):
    number = random.randrange(1, 500)
    write_Numbers.write(str(number) + "\n")
write_Numbers.close()
