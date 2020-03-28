# zad 4
import random
# TODO poprawić
print('---- zad 4 ------')


def gra():
    hidden_number = random.randint(0, 100)
    print(hidden_number)
    while True:
        user_number = int(input('Insert Number'))
        if hidden_number == user_number:
            # message to user
            break
        else:
            difference = abs(hidden_number - user_number)
            if difference > 50:
                print("Duza różnica > 50")
            elif difference > 10:
                print("Mniejsza roznica > 10")
            else:
                print("Mała różnica < 10")
