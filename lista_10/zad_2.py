POCZATEK = 5
KONIEC = 20


def print_numbers():
    global POCZATEK, KONIEC
    while True:
        print(POCZATEK)
        POCZATEK += 1
        if POCZATEK > KONIEC:
            break



if __name__ == '__main__':
    print_numbers()