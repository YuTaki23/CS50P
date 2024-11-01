import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')

    if p.match(ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()