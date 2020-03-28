# zad 3

numbers_list = [6, 8, 4, 5, 1, 9]


# def find_lower_number(numbers):
#     return min(numbers)

def find_lower_number(*numbers):
    min_number = numbers[0]
    for number in numbers:
        if min_number > number:
            min_number = number
    return min_number


if __name__ == '__main__':
    print(find_lower_number(1, 8, 9, -6, 5, 8, 9))
