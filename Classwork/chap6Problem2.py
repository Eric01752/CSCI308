#Opens file, then displays up to the first 5 lines
fileName = input("Enter the name of a file: ")

open_Filename = open(fileName, "r")

count = 0
while count < 5:
    data = open_Filename.readline()
    if data == "":
        break
    else:
        print(data, end="")
        count += 1
