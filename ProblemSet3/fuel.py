try:
    value = input("Fraction: ")
    x, z = value.split("/")
    a = int(x)
    b = int(z)
    c = a / b
    if (c > 0.99):
        print("F")
    elif (c < 0.01):
        print("E")
    else:
          print(f"{round(c):.2f}%")
except (ZeroDivisionError, ValueError):
    pass