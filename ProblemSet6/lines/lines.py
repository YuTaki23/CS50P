# lstrip 删除左边的空格
# startswith 检查字符串是否以指定字符串开头

import sys

def main():
    if (len(sys.argv) < 2):
        sys.exit("Too few command-line arguments")
    elif (len(sys.argv) > 2):
        sys.exit("Too many command-line arguments")
    else:
        if (sys.argv[1][-3:] != ".py"):
            sys.exit("Not a python file")
        else:
            print(count(sys.argv[1]))

def count(current_file):
    try:
        counter = 0
        with open(current_file, "r") as file:
            lines = file.readlines()

        for line in lines:
            if not (line.lstrip().startswith("#") or line.strip() == ""):
                counter += 1
        return counter
    except FileNotFoundError:
        sys.exit("File does not exit")

if __name__ == "__main__":
    main()