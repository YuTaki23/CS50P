GROCERY = []

while True:
    try:
        item = input().title()
        if item not in GROCERY:
            GROCERY.append(item)
    except EOFError:
        GROCERY.sort()
        for g in GROCERY:
            print(f"{GROCERY[g]}")
    except KeyError:
        pass
