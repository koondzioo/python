import argparse


def arg_parser():
    """Function to catch command line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--a',
                        help="side A",
                        type=int, required=True)
    parser.add_argument('--b',
                        help="side B",
                        type=int, required=True)
    parser.add_argument('--c',
                        help="side C",
                        type=int, required=True)
    return parser.parse_args()


def validate_length_sides(a, b, c):
    """Function validate possibility to create triangle"""
    # max_length = max(a, b, c)
    # min_length = min(a, b, c)
    # mid_length = max(min(a, b), min(max(a, b), c))
    min_length, mid_length, max_length = sorted(a, b, c) # !!!
    return max_length < min_length + mid_length


def calculate_circuit(a, b, c):
    """Function to calculate circuit triangle"""
    return a + b + c


# TODO wzór herona
def calculate_field(a, b, c):
    """Function to calculate field triangle"""
    return (a + b + c) * 0.5


def info_about_triangle(a, b, c):
    if a == b and a == c:
        print("trójkąt równoboczny")
    elif a != b and b != c and c != a:
        print("trójkąt róznoboczny")
    else:
        print("trójkąt równoramienny")


def info_about_angels_triangle(a, b, c):
    max_length = max(a, b, c)
    min_length = min(a, b, c)
    mid_length = max(min(a, b), min(max(a, b), c))
    if (max_length ** 2) == (min_length ** 2 + mid_length ** 2):
        print("trójkąt równoramienny")
    elif (max_length ** 2) > (min_length ** 2 + mid_length ** 2):
        print("trójkąt rozwartokątny")
    else:
        print("trójkąt ostrokatny")


# TODO twierdzenie cosinusow - oznacza boki trojkata o tej samej długości tym samym kolorem
# degrees(acos((A * A + B * B - C * C)/(2.0 * A * B)))
# turtle.pencolor("blue")
if __name__ == '__main__':
    print(info_about_angels_triangle(5, 7, 9))
