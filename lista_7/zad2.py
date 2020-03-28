from lista_7.zad1 import generate_random_temperature


def input_number():
    """Function to validate user input"""
    while True:
        print("How many temperatures you want to generate")
        value = input("Insert number: ")
        if value.isdigit():
            return int(value)


def save_to_file(file_name, temperatures):
    """Function save temperatures to file"""
    with open(file_name, "w") as f:
        for temp in temperatures:
            f.write('{}\n'.format(temp))

def main():
    n = input_number()
    list_celsius = [generate_random_temperature() for idx in range(n)]
    save_to_file('celsjusz.txt', list_celsius)


if __name__ == '__main__':
    main()
