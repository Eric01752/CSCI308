#Eric Schmidt
#Chapter 8: Problem 1

#Get sum of the string input
def sum(number):
    sum = 0
    for x in number:
        x = int(x)
        sum += x
    return sum

#Call sum function
def main():
    number = input("Enter a number: ")

    print(sum(number))

main()
