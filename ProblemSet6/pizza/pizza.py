import sys
import csv
from tabulate import tabulate

def main():
    # 需要一个命令行参数
    if (len(sys.argv) < 2):
        sys.exit("Too few command-lines.")
    elif (len(sys.argv) > 2):
        sys.exit("Too many command-lines.")
    else:
        if (sys.argv[1][-4:] != ".csv"):
            sys.exit("Not a csv file.")
        else:
            print(csv_to_ascii(sys.argv[1]))


def csv_to_ascii(current_file):
    try:
        with open(current_file) as file:
            csv_reader = csv.reader(file)
            table = tabulate(csv_reader, headers = "firstrow", tablefmt="grid")
            return table
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()