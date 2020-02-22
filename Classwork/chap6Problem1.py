#Opens file and prints all lines
open_Numbers = open("numbers.txt", "r")

for line in open_Numbers:
    number = int(line)
    print(number)
