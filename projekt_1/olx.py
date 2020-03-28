import json

import requests
from bs4 import BeautifulSoup

from flat import Flat

#TODO mozna uzyc selenium albo api olx
class OLX:
    def __init__(self, url):
        self.url = url
        self.response = requests.get(url)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        # self.flats = []
        self.dict_flats = {}

    def create_flat(self, flat_data):
        """Function create flat"""
        return Flat(self.find_title(flat_data), self.find_price(flat_data), self.find_district(flat_data),
                    self.find_renting_selling(flat_data), self.find_link(flat_data),
                    self.find_negotiations_allow(flat_data))

    def find_district(self, flat_data):
        """Function return flat district"""
        for small in flat_data.findAll('small', attrs={'class': 'breadcrumb x-normal'}):
            for sp in small.findAll(['span']):
                location = sp.find("i", {"data-icon": "location-filled"})
                if location:
                    return location.parent.text

    def find_link(self, flat_data):
        """Function return link to advertisement"""
        link = flat_data.find('a', attrs={'class': 'marginright5 link linkWithHash detailsLink'})
        if link:
            return link['href']
        link = flat_data.find('a', attrs={'class': 'marginright5 link linkWithHash detailsLinkPromoted'})
        if link:
            return link['href']

    def find_price(self, flat_data):
        """Function return flat price"""
        return flat_data.find('p', attrs={'class': 'price'}).text.strip()

    def find_title(self, flat_data):
        """Function return title advertisement"""
        return flat_data.find('div', attrs={'class': 'space rel'}).find('strong').text

    def find_renting_selling(self, flat_data):
        """Function return flat is for renting or selling"""
        option = flat_data.find('p', attrs={'class': "offer-path color-9 lheight16 margintop5"})
        return option.text.strip().split(' » ')[1]

    def find_negotiations_allow(self, flat_data):
        """Function return negotiation is allow"""
        if flat_data.find('span', attrs={'class': 'normal inlblk pdingtop5 lheight16 color-2'}):
            return flat_data.find('span', attrs={'class': 'normal inlblk pdingtop5 lheight16 color-2'}).text
        return 'Nie do negocjacji'

    def create_flats(self):
        """Function iterate over offers table and create flats"""
        offers_table = self.soup.find('table', attrs={'id': 'offers_table'})
        for flat_data in offers_table.find_all('tr', attrs={'class': 'wrap'}):
            # self.flats.append(self.create_flat(flat_data))
            self.create_dic_flat(flat_data)

    def create_dic_flat(self, flat_data):
        """Function create dictionary with flats data"""
        self.dict_flats.update({self.find_title(flat_data): {'title': self.find_title(flat_data),
                                                             'price': self.find_price(flat_data),
                                                             'district': self.find_district(flat_data),
                                                             'renting_or_selling': self.find_renting_selling(flat_data),
                                                             'link': self.find_link(flat_data),
                                                             'negotiation': self.find_negotiations_allow(flat_data)}})

    def save_to_file(self, file_name):
        """Function save data to json file"""
        with open(file_name + '.json', 'w', encoding='utf8') as f:
            json.dump(self.dict_flats, f, ensure_ascii=False)
