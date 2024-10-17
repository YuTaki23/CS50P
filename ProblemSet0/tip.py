def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    d = d.strip(d[0])
    d_float = float(d)
    return d_float
    
def percent_to_float(p):
    p = p[:-1]
    p_float = float(p)
    return p_float / 100

main()