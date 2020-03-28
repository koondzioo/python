from lista_7.zad1 import convert_celsius_to_fahrenheit


def read_from_file(file_name='celsjusz.txt'):
    """Function read temperatures from file"""
    with open(file_name, "r") as f:
        temp = f.read().splitlines()
    return temp


def save_to_file(temperatures):
    """Function save temperatures to file"""
    with open("fahrenheit.txt", "w") as f:
        for temp in temperatures:
            f.write('{}\n'.format(convert_celsius_to_fahrenheit(int(temp))))


def main():
    save_to_file(read_from_file())


if __name__ == '__main__':
    main()