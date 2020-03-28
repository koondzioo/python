import math
import random

KROWY = 0  # za poprawne odgagniecie z miejscem
BYKI = 0  # za zgadniecie ze liczba jest w numerze
DICT_ELEMENTS = {}
PROBY = 0
SET_POINTS = set()
# TODO refactor

def game():
    """function starts games"""
    print('Witaj w grze Krowy i Byki')
    random_number = 5551
    while True:
        number = input("Podaj liczbę ")
        number_user = create_array(int(number))
        if check_numbers(number_user, create_array(random_number)):
            pass
        else:
            break


# / vs // (Python2 and Python3)
def create_array(number):
    """create array of digits from number"""
    arr = []
    while number:
        arr.append(math.floor(number % 10))
        number //= 10
    return arr[::-1]


def check_numbers(number_user, number_random):
    """Function to count PROBY and management results BYKI, KROWY"""
    global PROBY, KROWY, BYKI
    if number_random == number_user:
        PROBY += 1
        print("Wygrales! Koniec Gry! Liczba prób: {}".format(PROBY))
        return False
    else:
        check_this_same_places(number_user, number_random)
        check_if_exsits(check_numbers_exstits_in_both_list(number_user, number_random))
        print("Krowy: {}, Byki: {}".format(KROWY, BYKI))
        PROBY += 1
        return True


def check_this_same_places(number_user, number_random):
    """add element with idx: value to dictionary if in both list have this same value and idx"""
    global KROWY, DICT_ELEMENTS
    for idx, (a, b) in enumerate(zip(number_user, number_random)):
        if a == b:
            if idx not in DICT_ELEMENTS.keys():
                KROWY += 1
                DICT_ELEMENTS.update({idx: a})
        else:
            pass


def check_numbers_exstits_in_both_list(number_user, number_random):
    """return list contains part of the common elements in lists (arg1, arg2) """
    return [item for item in number_user if item in number_random]


def check_if_exsits(arr):
    """check if element in array not exists in dict results add value to BYKI """
    global BYKI, DICT_ELEMENTS, SET_POINTS
    for el in arr:
        if el not in DICT_ELEMENTS.values() and el not in SET_POINTS:
            SET_POINTS.add(el)
            BYKI += 1


if __name__ == '__main__':
    game()
