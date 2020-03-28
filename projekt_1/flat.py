class Flat:
    def __init__(self, title, price, disctrict, renting_selling, link, negotiation='Nie do negocjacji'):
        self.title = title
        self.price = price
        self.district = disctrict
        self.renting_selling = renting_selling
        self.link = link
        self.negotiation = negotiation

    def print_flat(self):
        return f'tytuł: {self.title}, cena: {self.price}, dzielnica: {self.district}, wynajem/sprzedaz: {self.renting_selling}, link: {self.link}, negocjacje: {self.negotiation}'
