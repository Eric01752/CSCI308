males = int(input("Enter the number of males in class: "))
females = int(input("Enter the number of females in class: "))

total = males + females
males_percent = (males / total) * 100
females_percent = (females / total) * 100

print(f"Males: {males_percent}%\nFemales: {females_percent}%")
