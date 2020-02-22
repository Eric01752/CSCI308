import random

def main():
    even = 0
    odd = 0
    
    for x in range(100):
        number = random.randrange(1,100)
        if oddEvenCheck(number):
            even += 1
        else:
            odd += 1
    print("Even numbers: ", even)
    print("Odd numbers: ", odd)

##########################################

def oddEvenCheck(number):
    if number % 2 == 0:
        return True
    else:
        return False

main()
