#Eric Schmidt
#Chapter 7: Problem 1

#Get input from the user and store in a list
#Return: list
def inputStoreSales():
    sales = [0] * 7
    
    for x in range(7):
        saleAmount = int(input("Enter the store's sales for each day of the week: "))
        sales[x] = saleAmount
    return sales

#Display the list returned by function: inputStoreSales()
def main():
    count = 1
    
    for x in inputStoreSales():
        print("Day " + str(count) + ": " + str(x))
        count += 1

main()
