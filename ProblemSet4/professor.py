import random

def main():
    score = 0
    level = get_level
    chances = 3
    
    for _ in range(10):
        if (chances == 3):
            x, y = generate_integer(level)
        try:
            real_answer = int(x) + int(y)
            user_answer = int(input(f"{x} + {y} = "))
            
            if (real_answer == user_answer):
                score += 1
                continue
            else:
                raise ValueError
            
        except ValueError:
            print("EEE")
            chances -= 1
            pass
        
        if (chances == 0):
            print(f"{x} + {y} = {user_answer}")
            continue
        print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if (level != 1 or level != 2 or level != 3):
                continue
            else:
                return level
        except ValueError:
            pass
        except EOFError:
            break


def generate_integer(level):
    if (level == 1):
        x = random.randint(0, 9)
        y = random.randint(0, 9)

    elif (level == 2):
        x = random.randint(10, 99)
        y = random.randint(10, 99)

    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    return x, y


if __name__ == "__main__":
    main()