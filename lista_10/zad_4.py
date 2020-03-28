def count_letters():
    """Function counts vowels in string"""
    user_string = input('insert string: ')
    counter = 0
    for letter in ['A', 'E', 'I', 'O', 'U', 'Y']:
        counter += user_string.upper().count(letter)

    return counter


if __name__ == '__main__':
    print(count_letters())