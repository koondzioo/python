def list_of_sequence(n):
    """Function to create list of elements sequence"""
    return [element / (element + 1) for element in range(n)]


def save_to_file(numbers):
    """Function to save numbers to file"""
    with open("test.txt", "w") as f:
        for number in numbers:
            f.write('{}\n'.format(round(number, 2)))


if __name__ == '__main__':
    save_to_file(list_of_sequence(5))
