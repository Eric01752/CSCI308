#Eric Schmidt
#Quiz 1: Problem 1

PACKAGE_PRICE = 99

numPackages = int(input("Enter the number of packages purchased: "))
discount = 0

if numPackages >= 100:
    discount = .5
elif numPackages >= 50:
    discount = .4
elif numPackages >= 20:
    discount = .3
elif numPackages >= 10:
    discount = .2
else:
    discount = 0

packageDiscount = (numPackages * PACKAGE_PRICE) * discount
total = (numPackages * PACKAGE_PRICE) - packageDiscount
print("The discount is " + str(int(discount * 100)) + "%")
print("The total amount is $" + str(format(total, ".2f")))
