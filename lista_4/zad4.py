# zad 4

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# print(fib(9))


def fib2(n):
    if n == 0:
        return 0
    current_element = 1
    previous_element = 0
    for element in range(1, n):
        current_element, previous_element = current_element + previous_element, current_element
    return current_element


print(fib2(1))
