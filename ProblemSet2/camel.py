str = input("camelCase: ")
for word in str:
    if (word.isupper()):
        print("_" + word.lower(),end = "")
    else:
        print(word, end = "")