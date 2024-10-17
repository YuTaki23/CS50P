string = input("Input: ")
for word in string:
    if (word == "a" or word == "e" or word == "i" or word == "o" or word == "u"):
        print("", end = "")
    else:
        print(word, end = "")