from lista_5.arithmetic_sequence import n_arithmetic_sequence, sum_arithmetic_sequence


def validate_number(input_data):
    """Function to validate input is number"""
    if input_data.startswith('-'):
        return input_data.i
    else:
        return False


def insert_data(element):
    """Function to input value from terminal"""
    while True:
        value = input("Insert {} quadratic: ".format(element))
        if validate_number(value):
            return int(value)


def get_values():
    """Function to catch all values from user"""
    a1 = insert_data("a1")
    r = insert_data("r")
    n = insert_data("n")
    return a1, r, n


def init():
    """Main function"""
    a1, r, n = get_values()
    print(n_arithmetic_sequence(a1, r, n))
    print(sum_arithmetic_sequence(a1, r, n))


if __name__ == '__main__':
    init()
