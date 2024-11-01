from datetime import date, timedelta
import re
import sys
import inflect
import operator

p = inflect.engine()

def main():
    current_date = get_user_date(input("Date of Birth: "))
    difference = operator.sub(date.today(), date.fromisoformat(current_date))
    print(convert(difference.days))
    
def convert(time):
    minutes = time * 24 * 60
    return f"{(p.number_to_words(minutes))} minutes"
    
def get_user_date(date):
    if not correct_date(date):
        sys.exit("Invalid Date.")
    else:
        return date    

def correct_date(date):
    p = re.compile(r"(\d{4}-\d{1,2}-\d{1,2})")

    if (p.match(date)):
        return True
    else:
        return False

if __name__ == "__main__":
    main()