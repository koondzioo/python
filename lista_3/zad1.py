# zad 1

# funkcja index ! -> nie uzywac zmiennej index
numbers = [element**2 for element in range(1, 100)]
for idx, number in enumerate(numbers, 1):
    print('index: {}, number {}'.format(idx, idx * idx))
