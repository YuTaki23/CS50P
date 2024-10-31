def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    while True:
        try:
            x, y = map(int, fraction.split("/"))
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError
            return round(x / y * 100)
        except (ValueError, ZeroDivisionError):
            pass
        

def gauge(percentage):
    string = ""
    if (percentage <= 1):
        string = "E"
    elif (percentage >= 99):
        string = "F"
    else:
        string = str(percentage) + "%"

    return string


if __name__ == "__main__":
    main()