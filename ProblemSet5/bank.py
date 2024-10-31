def main():
    greeting = input("Greeting: ")
    print(value(greeting))

def value(greeting):
    value = ""
    new_greeting = greeting.strip().lower()

    if (new_greeting[0:5] == "hello"):
        value = "$0"
    elif (new_greeting[0:1] == "h"):
        value = "$20"
    else:
        value = "$100"
    return value

if __name__ == "__main__":
    main()