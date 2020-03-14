#Eric Schmidt
#Chapter 8: Problem 3

#Counts the number of lines and words to get average number of words per sentence
def main():
    sentence_txt = open("sentence.txt", "r")

    lineCount = 0
    wordCount = 0
    while True:
        line = sentence_txt.readline()
        if line == "":
            break
        line = line.split()
        for x in line:
            wordCount += 1
        lineCount += 1

    sentence_txt.close()
    average = wordCount // lineCount

    print("Average number of words is", average)

main()
