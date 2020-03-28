

def calculate_capacity(a, *args):
    """Function to calculate capacity"""
    if not args:
        return a**3
    else:
        b, c = args
        return a * b * c



if __name__ == '__main__':
    print(calculate_capacity(3, 2, 3))
