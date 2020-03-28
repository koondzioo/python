# zad 2
# i = 0
#
# # przerobic można szybciej
# # drukujemy wszystkie liczby parzyste mniejsze od 10
# while i < 10:
#     if i % 2:  # reszta z dzielenia != 0 -> True
#         pass
#         # continue    # pomiń liczby nieparzyste ---> Continue wraca do początku pętli while !!!!
#     else:
#         print(i)  # drukuj liczby parzyste
#     i += 1  # zwiększ i o jeden

i = 0
while i < 10:
    if not i % 2:
        print(i)
    i += 1
print('----')
# print([even for even in range(0, 10, 2)])
