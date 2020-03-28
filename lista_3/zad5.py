import turtle
# zad 5

# czemu nie uzywac eval() - funkcja ta pozwala na uruchomienie kodu pythona wewnatrz siebie - interpretuje podany string jakos kod pythonowy

def draw_square():
    length = eval(input("Podaj dł\lugosc boku: "))
    n_sides = 4  # ilosc boków
    turtle.speed(20)  # ustal predkosc zolwia
    # powtorz n_sides razy
    for idx in range(n_sides):
        turtle.forward(length)  # narysuj linie o danej dlugosci
        turtle.right(90)  # obroc sie w prawo o dany kat
    turtle.mainloop()  # nie zamykaj okna po narysowaniu


def draw_tringle():
    length = eval(input("Podaj dł\lugosc boku: "))
    n_sides = 3  # ilosc boków
    turtle.speed(20)  # ustal predkosc zolwia
    # powtorz n_sides razy
    for idx in range(n_sides):
        turtle.forward(length)  # narysuj linie o danej dlugosci
        turtle.right(120)  # obroc sie w prawo o dany kat
    turtle.mainloop()  # nie zamykaj okna po narysowaniu

def draw_hexagon():
    length = eval(input("Podaj dł\lugosc boku: "))
    n_sides = 6  # ilosc boków
    turtle.speed(20)  # ustal predkosc zolwia
    # powtorz n_sides razy
    for idx in range(n_sides):
        turtle.forward(length)  # narysuj linie o danej dlugosci
        turtle.right(60)  # obroc sie w prawo o dany kat
    turtle.mainloop()  # nie zamykaj okna po narysowaniu

def draw_shape():
    length = eval(input("Podaj dł\lugosc boku: "))
    n_sides = eval(input("Podaj liczbe bokow (min. 3) "))
    turtle.speed(20)  # ustal predkosc zolwia
    # powtorz n_sides razy
    for idx in range(n_sides):
        turtle.forward(length)  # narysuj linie o danej dlugosci
        turtle.right(360/n_sides)  # obroc sie w prawo o dany kat
    turtle.mainloop()  # nie zamykaj okna po narysowaniu
