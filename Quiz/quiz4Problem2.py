#Eric Schmidt
#Quiz 4: Problem 2

def vowels(inString):
    vowels = "AaEeIiOoUu"
    count = 0
    for x in inString:
        if x in vowels:
            count += 1
    return count

def consonants(inString):
    consonants ="BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxZz"
    count = 0
    for x in inString:
        if x in consonants:
            count += 1
    return count

def main():
    string = input("Enter a string: ")

    print("Number of vowels:", vowels(string))
    print("Number of consonants:", consonants(string))

main()
