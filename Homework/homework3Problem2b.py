#Eric Schmidt
#Homework 3: Problem 2b

#Create file object
golf_txt = open("golf.txt", "r")

#Get data from file
data = golf_txt.read()

#Display the data
print(data)

#Close file object
golf_txt.close()
