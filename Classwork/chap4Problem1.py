CALORIES_BURNED = 4.2

check = True
count = 1
totalCalories = 0

while check:
    totalCalories += CALORIES_BURNED
    if count == 10:
        print("Calories burned at 10 minutes: " + str(format(totalCalories, ".2f")))
    elif count == 15:
        print("Calories burned at 15 minutes: " + str(format(totalCalories, ".2f")))
    elif count == 20:
        print("Calories burned at 20 minutes: " + str(format(totalCalories, ".2f")))
    elif count == 25:
        print("Calories burned at 25 minutes: " + str(format(totalCalories, ".2f")))
    elif count == 30:
        print("Calories burned at 30 minutes: " + str(format(totalCalories, ".2f")))
        check = False
    count = count + 1
    
