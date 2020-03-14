#Eric Schmidt
#Quiz 4: Problem 1

import re

def sentenceLowercase(inString):
    tempString = re.findall("[A-Z][^A-Z]*", inString)

    outString = ""
    for x in tempString:
        outString += (x + " ")
    return outString

def main():
    string = input("Enter a string with no spaces and each first letter capitalized: ")

    print(sentenceLowercase(string))

main()
