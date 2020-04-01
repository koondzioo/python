import matplotlib.pyplot as plt

class Samochod():

    def __init__(self, maksymalna_predkosc, spalanie):
        """ Returns the Car Object.

          Parameters:
              maksymalna_predkosc (int):maximum speed car
              spalanie (int): combustion car

          Returns:
              Object Samochod
         """
        self.maksymalna_predkosc = maksymalna_predkosc
        self.spalanie = spalanie
        self.obecna_predkosc = 0
        self.pokonany_dystans = 0
        self.czas_podrozy = 0
        self.id_podrozy = 1
        self.dane_trasy = {}

    def dodaj_dane(self, czas_podrozy, pokonany_dystans, predkosc):
        self.dane_trasy.update({self.id_podrozy: {'czas_podrozy': czas_podrozy,
                                                  'pokanany_dystans': pokonany_dystans,
                                                  'predkosc': predkosc}})
        self.id_podrozy += 1

    def przyspiesz(self, wartosc):
        """Function to increase speed"""
        if self.obecna_predkosc + wartosc > self.maksymalna_predkosc:
            self.obecna_predkosc = self.maksymalna_predkosc
        else:
            self.obecna_predkosc += wartosc

    def zwolnij(self, wartosc):
        """Function to decrease speed"""
        if self.obecna_predkosc - wartosc < 0:
            self.obecna_predkosc = 0
        else:
            self.obecna_predkosc -= wartosc

    def hamuj(self):
        """Function to stop car"""
        self.obecna_predkosc = 0

    def turbo(self):
        """Function increases to maximum speed car"""
        self.obecna_predkosc = self.maksymalna_predkosc

    def jedz(self, wartosc):
        """Function to calculate distance and travel time"""
        self.pokonany_dystans += wartosc
        self.czas_podrozy += wartosc / self.obecna_predkosc
        self.dodaj_dane(wartosc / self.obecna_predkosc, wartosc, self.obecna_predkosc)

    def print_samochod(self):
        """Function to print object Car"""
        return 'maksymalna_predkosc: {}, spalanie: {}, obecna_predkosc: {}, pokonany_dystans: {}, czas_podrozy: {}'.format(
            self.maksymalna_predkosc, self.spalanie, self.obecna_predkosc, self.pokonany_dystans, self.czas_podrozy)

    def print_dane_trasy(self):
        for k, v in self.dane_trasy.items():
            print(k)
            for kk, vv in v.items():
                print(f'{kk}, {vv}')

    # https://matplotlib.org/index.html
    def print_graph(self):
        x = [element['czas_podrozy'] for element in self.dane_trasy.values()]
        y = [element['pokanany_dystans'] for element in self.dane_trasy.values()]
        print(x)
        print(y)
        plt.xlabel('Czas podrozy[h]')
        plt.ylabel('Pokonany dystans [km]')
        plt.title('Stosunek dystansu od czasu')
        plt.grid(True)
        plt.plot(x, y)
        plt.show()

if __name__ == '__main__':
    samochod = Samochod(200, 10)
    samochod.przyspiesz(100)
    samochod.jedz(100)
    samochod.turbo()
    samochod.jedz(150)
    samochod.jedz(70)
    samochod.jedz(170)
    samochod.jedz(120)
    samochod.print_dane_trasy()
    samochod.print_graph()
    print(samochod.print_samochod())
