def main():
    string = input("Input: ")
    print(shorten(string))


def shorten(word):
    string = ""
    for letter in word:
        if (letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u"):
            #print("", end = "")
            string = string + ""
        else:
            #print(letter, end = "")
            string = string + letter

    return string

if __name__ == "__main__":
    main()