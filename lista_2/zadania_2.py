import sys

# zad 1
numbers = (0, 1, 2, 3, 4, "piec", "szesc", "siedem", "osiem", "dziewiec")
print(numbers[:3])
print(numbers[-2:])
print(numbers[1::2])
print(len(numbers))
print(len(numbers[-2]))
# ?? ?? ??
print(numbers[:5] + (5, 6) + numbers[-3:])  # zmienne pod 5, 6 został zmianione i "połączone"
print(numbers[:5], (5, 6), numbers[-3:])    # zostały podzielone na 3 oddzielne krotki
# numbers.append("")  -> krotka nie posiada funkcji append (error)
#tuple jest immutable, nie można rozszerzać ani usuwać nic po zdefiniowaniu takiej zmiennej.
new_item = ("",)
print(numbers + new_item)

# zad 2
students = ["Kasia", "Basia", "Marek", "Darek"]
students.append("Józek")
students.extend(["Ania", "Basia"])
print(students)
# students = students.sort() --> zwraca None
# students = sorted(students) --> zwraca posortowana liste do zmiennej
students.sort()
print(students)
print(students[3])
print(students[:2])
print(students[:-2])
print('---')
students_set = set(students)
students_set.discard("Basia")
print(students_set)
print(len(students_set))
students_tuple = tuple(students_set)
print(type(students_tuple))
# Zad 3
# numbers_of_three = []
# for number in range(0, 100, 3):
#     numbers_of_three.append(number)
numbers_of_three = list(range(0, 100, 3))   # ---> szybsze tworzenie listy
print(numbers_of_three)

del numbers_of_three[5: len(numbers_of_three): 3]
print(numbers_of_three)

print(sum(numbers_of_three)/len(numbers_of_three))


# zad 4
krotka = ('a', 'b', 'c', 'd')
# meoda str.join pozwala na łączenie znaków z tablic, tuple itp. (elementy iterable) w jeden ciąg
print("".join(krotka))
print(" ".join(krotka))
print(", ".join(krotka))

answer = '\t'.join('0' for i in (range(0, 100)))
# answer = '0\t' * 100 --> proste rozwiazanie :)
print(answer)

# zad 5
slubowanie = """
wstępując do wspólnoty akademickiej Uniwersytetu Wrocławskiego, ślubuję uroczyście:
- zdobywać wiedzę i umiejętności,
- postępować zgodnie z prawem, tradycją i dobrymi obyczajami akademickimi,
- dbać o dobre imię Uniwersytetu Wrocławskiego i godność studenta.
"""
print(slubowanie)
#slubowanie w konsoli wyświelta wraz z ukrytym znakai "\n"
#print(slubowanie[0]) ---> nie wyswietla nic nie ma elementu pod zadanym indeksem
slubowanie = slubowanie[1].upper() + slubowanie[2:]  # nowa zmienna

print(slubowanie)
print(slubowanie.count(' i '))
print(slubowanie.count('i'))
print("Uniwersytet" in slubowanie)
arr = slubowanie.split(' ')
print(len(arr))
arr2 = slubowanie.split('\n')
print(len(arr2))
# zad 6
print('=== zad 6 ====')
print(sys.getsizeof(0))
print(sys.getsizeof(2 ** 100))
print(sys.getsizeof(2 ** 1000))
print(sys.getsizeof(True))
print(sys.getsizeof(False))
#isinstance() - sprawdza czy dany objekt jest konkretnego typu
print(isinstance(('',), tuple))
print(isinstance(0, int))
print(isinstance(0, float))
print(isinstance(0.0, float))
print(isinstance(True, bool))
print(isinstance(True, int))
# zad 7
print('----- zad 7 ------')
x = 2
y = x
print(x, y, id(x), id(y))
y = 3
print(x, y, id(x), id(y))
print('------')
x = [1,2]
y = x
print(x, y, id(x), id(y))
y[1] = 3
print(x, y, id(x), id(y))
# spowodowane jest to tym że listy w pythonie są mutable i można zmieniać w nich wartości
# (nie powoduje to zajęcia nowego miejsca w pamięci jak w przypadku int)
# zad 8
print('----- zad 8 ------')
xx = (aa, bb, cc) = (1, 2, 3)
print(xx)
print(aa)
print(bb)
print(cc)
xxx = aaa, bbb, ccc = 1, 2, 3
print(xxx)
print(aaa)
print(bbb)
print(ccc)



zmienna_a = 1
zmienna_b = "jeden"
zmienna_a, zmienna_b = zmienna_b, zmienna_a
# tmp = zmienna_a
# zmienna_a = zmienna_b
# zmienna_b = tmp
print(zmienna_a)
print(zmienna_b)