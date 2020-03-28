def collatz_even(number):
    """Function to calculate"""
    return 0.5 * number


def collatz_odd(number):
    """Function to calculate"""
    return (3 * number) + 1


def function1(c0, n):
    for element in range(n):
        if c0 % 2 == 0:
            c0 = collatz_even(c0)
        else:
            c0 = collatz_odd(c0)
        print(c0)


def zad4(c0):
    print(c0)
    while True:
        if c0 % 2 == 0:
            c0 = collatz_even(c0)
        else:
            c0 = collatz_odd(c0)
        print(c0)
        if c0 == 1:
            break



def main():
    zad4(11)

# TODO map() i ord()
# ord() - zwraca wartość z tablicy ASCII
if __name__ == '__main__':
    main()
