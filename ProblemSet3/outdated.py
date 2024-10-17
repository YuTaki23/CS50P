months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    Date = input("Date: ")
    try:
        if (Date.find("-")):
            month, date, year = Date.split("/")
            if (1 <= int(month) <= 12 and 1 <= int(date) <= 31):
                break        

        elif (Date.find(",")):
            Date = Date.replace(",", "")
            month, date, year = Date.split(" ")
            if (month in  Date and 1 <= int(date) <= 31):
                break

    except:
        print()
        pass

print(f"{int(year):04}--{int(month):02}--{int(date):02}")