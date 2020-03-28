# def arithmetic_sequence(a1, r, n):
#     """Function to calculate arithmetic sequence"""
#     return [(a1 + (element - 1) * r) for element in range(a1, n + 1)]


def n_arithmetic_sequence(a1, r, n):
    return a1 + (n - 1) * r


def sum_arithmetic_sequence(a1, r, n):
    return sum([n_arithmetic_sequence(a1, r, element) for element in range(a1, n + 1)])
