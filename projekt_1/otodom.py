import json

from bs4 import BeautifulSoup
import requests

from flat import Flat


class OTODOM:
    def __init__(self, url):
        self.url = url
        self.response = requests.get(url)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        # self.flats = []
        self.dict_flats = {}

    def create_flat(self, flat_data):
        """Function create flat from advertisement"""
        return Flat(self.find_title(flat_data), self.find_price(flat_data), self.find_district(flat_data),
                    self.find_renting_selling(flat_data), self.find_link(flat_data))

    def find_district(self, flat_data):
        """Function return flat district"""
        return flat_data.find('p', attrs={'class': 'text-nowrap'}).text.split(': ')[1]

    def find_link(self, flat_data):
        """Function return link to advertisement"""
        return flat_data['data-url']

    def find_price(self, flat_data):
        """Function return flat price"""
        return flat_data.find('li', attrs={'class': 'offer-item-price'}).text.strip()

    def find_title(self, flat_data):
        """Function return title advertisement"""
        return flat_data.find('span', attrs={'class': 'offer-item-title'}).text

    def find_renting_selling(self, flat_data):
        """Function return flat is for renting or selling"""
        return flat_data.find('p', attrs={'class': 'text-nowrap'}).text.split(': ')[0].split(' ')[2]

    def create_flats(self):
        """Function create list flats"""
        for flat_data in self.soup.find_all('article'):
            # self.flats.append(self.create_flat(flat_data))
            self.create_dic_flat(flat_data)

    def create_dic_flat(self, flat_data):
        """Function create dictionary with flats data"""
        self.dict_flats.update({self.find_title(flat_data): {'title': self.find_title(flat_data),
                                                             'price': self.find_price(flat_data),
                                                             'district': self.find_district(flat_data),
                                                             'renting_or_selling': self.find_renting_selling(flat_data),
                                                             'link': self.find_link(flat_data),
                                                             'negotiation': 'Nie do negocjacji'}})

    def save_to_file(self, file_name):
        """Function save data to json file"""
        with open(file_name + '.json', 'w', encoding='utf8') as f:
            json.dump(self.dict_flats, f, ensure_ascii=False)
