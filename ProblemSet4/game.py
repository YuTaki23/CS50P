import random

while True:
    try:
        user_num = int(input("Level: "))
        random_num = random.randint(1, user_num)
        
        while True:
            guess_num = int(input("Guess: "))
            if guess_num > user_num:
                print("Too large!")
            elif guess_num < user_num:
                print("Too small!")
            elif guess_num == user_num:
                print("Just right!")
                raise EOFError
        
    except ValueError:
        pass
    except EOFError:
        break