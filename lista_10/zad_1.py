POCZATEK = 5
KONIEC = 20


def print_numbers():
    global POCZATEK, KONIEC
    for number in range(POCZATEK, KONIEC+1):
        print(number)



if __name__ == '__main__':
    print_numbers()