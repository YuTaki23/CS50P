
def calculator(x, y, z):
    if (y == "+"):
        return x + z
    elif (y == "-"):
        return x - z
    elif (y == "*"):
        return x * z
    else:
        if(z == 0):
            print("0 can not be a divisor")
        else:
            return x / z

def main():
    expression = input("Expression: ").strip()
    x, y, z = expression.split(" ")
    
    print(f"{calculator(int(x), y, int(z)):.1f}")

if (__name__ == "__main__"):
    main()