import math


def validate_number(input_data):
    """Function to validate input is number"""
    if input_data.startswith('-'):
        return input_data[1:].isdigit()
    return input_data.isdigit()


def insert_data(element):
    """Function to input value from terminal"""
    while True:
        value = input("Insert {} quadratic: ".format(element))
        if validate_number(value):
            return int(value)


def get_values():
    """Function to catch points from user"""
    a = insert_data('a')
    b = insert_data('b')
    c = insert_data('c')
    return a, b, c


def calculate_x1(a, b, delta):
    """Function to calculate x1 formula: -b-sqrt(delta)/2a"""
    return (-b - math.sqrt(delta)) / (2 * a)


def calculate_x2(a, b, delta):
    """Function to calculate x1 formula: -b+sqrt(delta)/2a"""
    return (-b + math.sqrt(delta)) / (2 * a)


def calculate_x(a, b):
    """Function to calculate x formula: -b/2a"""
    return -b / (2 * a)


def print_result(a, b, delta):
    """Function to print result after calculate"""
    if delta > 0:
        x1 = calculate_x1(a, b, delta)
        x2 = calculate_x2(a, b, delta)
        print('x1: {}, x2: {}'.format(x1, x2))
    else:
        x = calculate_x(a, b)
        print('x: {}'.format(x))


def calculate_delta(a, b, c):
    """Function to calculate delta formula: b^2-4ac"""
    return math.pow(b, 2) - (4 * (a * c))


def main():
    """Main function quadratic equation"""
    a, b, c = get_values()
    if b == 0 or c == 0:
        print("Incomplete quadratic equation")
    else:
        print("complete quadratic equation")
    delta = calculate_delta(a, b, c)

    print_result(a, b, delta)


if __name__ == '__main__':
    main()
