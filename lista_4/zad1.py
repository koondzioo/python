# zad1
product = {
    "chleb": 20,
    "piwo": 100,
    "mleko": 120,
    "marchewka": 95,
    "wino": 120
}


def print_dict(product):
    for product_name, price in product.items():
        print('{} --> cena: {}'.format(product_name, price))


def average_price(product):
    return sum(product.values()) / len(product.values())


print_dict(product)

print(average_price(product))

product.update({"papierosy": 150})
product['papierosy'] = 150

print_dict(product)fib

print(average_price(product))

del product['papierosy']

print_dict(product)

print(average_price(product))