def main():
    time = input("What time is it?")
    current_time = convert(time)
    if (7 <= current_time <= 8):
        print("breakfast time")
    elif (12 <= current_time <= 13):
        print("lunch time")
    elif (18 <= current_time <= 19):
        print("dinner time")
    else:
        print("Not time for eating.")



def convert(time):
    x, y = time.split(":")
    if (float(y) == 0):
        return float(x)
    else:
        return float(x) + (60 / float(y))


if __name__ == "__main__":
    main()