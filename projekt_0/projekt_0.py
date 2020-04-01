import math


def input_number():
    """Function to validate user input"""
    while True:
        value = input("Podaj liczbę ")
        if value.isdigit():
            return int(value)


def create_numbers(random_number):
    """Function to create numbers to game"""
    number = input_number()
    number_user = create_list_from_number(int(number))
    number_random = create_list_from_number(random_number)
    return number_random, number_user


def create_list_from_number(number):
    """create list of digits from number"""
    separate_number = []
    while number:
        separate_number.append(math.floor(number % 10))
        number //= 10
    return separate_number[::-1]


def count_attemps(number_user, number_random, helpers):
    """Function to count attempts and management results bulls and cows"""
    if number_random == number_user:
        helpers[2] += 1
        print("Wygrales! Koniec Gry! Liczba prób: {}".format(helpers[2]))
        return False
    else:
        helpers = count_points(number_random, number_user, helpers)
        print("Krowy: {}, Byki: {}".format(helpers[0], helpers[1]))
        helpers[2] += 1
        print('proby {}'.format(helpers[2]))
        return True


def count_points(number_random, number_user, helpers):
    """Function count cows, bulls and update dict and set points"""
    helpers[0], helpers[3] = count_cows(number_user, number_random, helpers)
    helpers[1], helpers[3], helpers[4] = count_bulls(find_commons_elements(number_user, number_random), helpers)
    return helpers


def count_cows(numbers_user, numbers_random, helpers):
    """add element with idx: value to dictionary if in both list have this same value and idx"""
    cows, dict_elements = helpers[0], helpers[3]
    for idx, (digit_user, digit_random) in enumerate(zip(numbers_user, numbers_random)):
        if digit_user == digit_random:
            if idx not in dict_elements.keys():
                cows += 1
                dict_elements.update({idx: digit_user})
    return cows, dict_elements


def find_commons_elements(number_user, number_random):
    """return list contains part of the common elements in lists (arg1, arg2) """
    return [item for item in number_user if item in number_random]


def count_bulls(commons_elements, helpers):
    """check if element in list not exists in dict results add value to BYKI """
    bulls, dict_elements, set_points = helpers[1], helpers[3], helpers[4]
    for element in commons_elements:
        if element not in dict_elements.values() and element not in set_points:
            set_points.add(element)
            bulls += 1
    return bulls, dict_elements, set_points


def main():
    """function starts games"""
    cows = 0
    bulls = 0
    dict_elements = {}
    attempts = 0
    set_points = set()
    #TODO rozbic z tablicy
    helpers = [cows, bulls, attempts, dict_elements, set_points]
    print('Witaj w grze Krowy i Byki')
    random_number = 3393
    while True:
        number_random, number_user = create_numbers(random_number)
        if not count_attemps(number_user, number_random, helpers):
            break


if __name__ == '__main__':
    main()
