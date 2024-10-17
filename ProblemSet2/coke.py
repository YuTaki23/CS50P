total = 50
while (total > 0):
    print(f"Amount Due: {total}")
    insert = input("Insert Coin: ")
    total = total - int(insert)
    
if (total <= 0):
    print(f"Changed Owed: {total}")