#Eric Schmidt
#Chapter 7: Problem 2

#Get data from charge_accounts.txt and store in list
#Return: list
def readChargeAccounts():
    accountNumberList = []
    chargeAccounts_txt = open("charge_accounts.txt", "r")

    while True:
        number = chargeAccounts_txt.readline()
        if number == "":
            break
        number = int(number.strip("\n"))
        accountNumberList.append(number)

    chargeAccounts_txt.close()
    return accountNumberList

#Ask user for an account number
#Check to see if account number is in list
def main():
    accountNumberList = []
    accountNumberList += readChargeAccounts()

    number = int(input("Enter a charge account number: "))
    if number in accountNumberList:
        print("The number is valid.")
    else:
        print("The number is invalid.")

main()
