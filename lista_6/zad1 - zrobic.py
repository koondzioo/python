# range -- list
# TODO
def geometric_sequence(a1, q, n):
    return [el * q for el in range(a1, n)]




if __name__ == '__main__':
    print(geometric_sequence(1, 3, 5))