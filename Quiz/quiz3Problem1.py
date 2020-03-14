#Eric Schmidt
#Quiz 3: Problem 1

def perfect(number):
    sum = 0
    for x in range(1,number):
        if number % x == 0:
            sum += x
    if sum == number:
        return True
    else:
        return False

def displayFactors(number):
    for x in range(1,number):
        if number % x == 0:
            print(str(x), end=" ")

def main():
    print("The perfect numbers in {1, 1000} are: ")
    for x in range(1,1000):
        if perfect(x) == True:
            print(str(x) + " = ", end="")
            displayFactors(x)
            print()

main()
