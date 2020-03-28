def is_prime(number):
    """Function to check number is prime"""
    for element in range(2, number):
        if number % element == 0:
            return False
    return True


def main():
    """Function to input value from terminal"""
    while True:
        value = input("Insert number: ")
        if is_prime(int(value)):
            print("Ok, number is prime")
            break
        print("Try again, number is not prime")


if __name__ == '__main__':
    main()
