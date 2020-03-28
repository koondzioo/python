# zad 3

# lista zakupów
grocery = ['jajka', 'mleko', 'chleb', 'maslo', 'piwo']
# ilość sztuk
n_items = {}
# zakazane produkty
prohibited = ['wódka', 'piwo', 'wino']

# w pętli pytamy użytkownika, ile sztuk danego produktu chce kupić
for product in grocery:
    n_items[product] = 0
    if product not in prohibited:
        n_items[product] = input('{}, ile sztuk dodać do koszyka? '.format(product))  # można dodać walidację inputa
    # input('ile sztuk?')
    # wydrukuj na ekranie komunikat: "Produkt [nazwa produktu]: sztuk = "
    # pobierz liczbę od użytkownika i zapisz w n_items dla danego produktu
    # pomiń produkty zakazane (i automatycznie przyjmij ilość = 0)

for idx, (k, v) in enumerate(n_items.items(), start=1):
    print('{}. {}: {}'.format(idx, k, v))
    
# w pętli wydrukuj: [lp]. [nazwa produktu]: [ilość]
# czyli np.: 1. jajka: 5 itd.
