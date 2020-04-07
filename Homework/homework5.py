#Eric Schmidt
#Homework 5

def main():

    #Create file handling objects
    text_file = open("Kennedy.txt", "r")
    index_file = open("index.txt", "w")
    
    #Create dictionary and line number variable
    indexDict = dict()
    lineNumber = 1

    #Read the text file line by line and store each word in dictionary
    #with it's line number(s)
    while True:
        line = text_file.readline()
        if line == "":
            break
        lineList = line.strip("\n").split(" ")
        for word in lineList:
            if word in indexDict.keys():
                if lineNumber in indexDict[word]:
                    pass
                else:
                    indexDict[word].append(lineNumber)
            else:
                indexDict[word] = [lineNumber]
        lineNumber += 1
        
    text_file.close()

    #Get all items in dictionary and write to index.txt file
    for key, value in indexDict.items():
        lineNumbers = ""
        for number in value:
            lineNumbers += str(number) + " "
        index_file.write(key + ": " + lineNumbers + "\n")

    index_file.close()

main()
