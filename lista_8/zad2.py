def generate_sequence(n):
    return (element / (element + 1) for element in range(n))


# TODO Generatory poczytac jak dziala (iterator, yaild itp.)
if __name__ == '__main__':
    for i in generate_sequence(5):
        print(i, end=', ')