#Eric Schmidt
#Quiz 3: Problem 2

sum = 0
count = 0

try:
    numbers_txt = open("numbers.txt", "r")

    print("File contents: ", end="")
    while True:
        line = numbers_txt.readline()
        number = line.strip()
        if number == "":
            break
        else:
            sum += int(number)
            count += 1
            print(str(number) + " ", end="")
except IOError:
    print("IO Error")
except ValueError:
    print("Value Error")

numbers_txt.close()

print()
print("Total: " + str(sum))
print(str(count) + " numbers were read from the file.")
