def convert(str):
    dictionary = {
        ":": None,
        ")": "🙂",
        "(": "🙁",
    }
    transTable = str.maketrans(dictionary)
    new_str = str.translate(transTable)
    print(new_str)

def main():
    convert(input("Please enter a sentence."))

if __name__ == "__main__":
    main()