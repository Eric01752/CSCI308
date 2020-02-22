#Eric Schmidt
#Quiz 2: Problem 1

PERCENT_INCREASE = .03

tuition = 8000
yearIncrease = 0
count = 1

for x in range(5):
    print("Year ", count, ": $", format(tuition, ".2f"), sep="")
    yearIncrease += tuition * PERCENT_INCREASE
    tuition += yearIncrease
    count += 1
