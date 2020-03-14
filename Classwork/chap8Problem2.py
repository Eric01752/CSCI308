#Eric Schmidt
#Chapter 8: Problem 2

#Convert the date from input to new format
#Return: newDate
def convertDateFormat(date):
    date = date.split("/")

    monthList = ["Jan", "Feb", "Mar", "May", "Jun", "Jul", "Aug", "Sep", "Nov", "Dec"]

    month = int(date[0])
    day = date[1]
    year = date[2]

    monthName = monthList[month - 1]

    newDate = monthName + " " + day + ", " + year
    return newDate

#Calls the convertDateFormat function
def main():
    date = input("Enter a date in format-(mm/dd/yyyy): ")

    print(convertDateFormat(date))

main()
