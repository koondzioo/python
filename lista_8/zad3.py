import sys

from lista_8.zad1 import list_of_sequence
from lista_8.zad2 import generate_sequence




if __name__ == '__main__':
    # List comprehensions zwraca liste elementów czesto zajmuje wiecej miejsca  w pamieci od generatora
    # generator expressions - zwraca iterator

    list_5_elements = list_of_sequence(5)
    gen_5_elements = generate_sequence(5)
    print(sys.getsizeof(list_5_elements))
    print(sys.getsizeof(gen_5_elements))
    print('------')
    list_10_elements = list_of_sequence(10)
    gen_10_elements = generate_sequence(10)
    print(list_10_elements)
    print(gen_10_elements)
    print(sys.getsizeof(list_10_elements))
    print(sys.getsizeof(gen_10_elements))
    list_1000_elements = list_of_sequence(1000)
    gen_1000_elements = generate_sequence(1000)
    print(list_1000_elements)
    print(gen_1000_elements)
    print(sys.getsizeof(list_1000_elements))
    print(sys.getsizeof(gen_1000_elements))