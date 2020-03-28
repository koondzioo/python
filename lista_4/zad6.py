def print_arg(number, *args):
    print(number)
    for idx, element in enumerate(args, start=1):
        print('{} -> {}'.format(idx, element))


def print_dict(**kwargs):
    for key, value in kwargs.items():
        print('{} -> {}'.format(key, value))


if __name__ == '__main__':
    print_arg(1, 2, 3, 4, 5)
    print_dict(one=1, two=2, three=3)
