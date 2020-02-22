#Opens a file and calculates average of all numbers
open_Numbers = open("numbers.txt", "r")

average = 0

for number in open_Numbers:
    average += int(number)
print("Average: ", average)
