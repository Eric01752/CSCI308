#Eric Schmidt
#Homework 4: Problem 2

import re

#Capitalizes the first word for each sentence
#Prints the resulting string
def sentenceCapitalize(inString):
    tempString = re.split("([.!?])", inString)
    
    outString = ""
    for x in tempString:
        if x == "." or x == "!" or x == "?":
            outString += x
            outString += " "
        else:
            outString += x.lstrip().capitalize()
    
    print(outString)

#Gets input from user
#Calls the sentenceCapitalize function
def main():
    string = input("Enter a string of multiple sentences: ")

    sentenceCapitalize(string)

main()
