#Eric Schmidt
#Homework 3: Problem 2a

#Create file object
golf_txt = open("golf.txt", "w")

#Get input from user and write to file
while True:
    name = input("Enter the player name(q to quit): ")
    if name == "q":
        break
    score = int(input("Enter the player score: "))
    golf_txt.write(str(name) + " " + str(score) + "\n")

#Close file object
golf_txt.close()
