greet = input("Greeting: ")
new_greet = greet.strip().lower()

if (new_greet[0:5] == "hello"):
    print("$0")
elif (new_greet[0:1] == "h"):
    print("$20")
else:
    print("$100")