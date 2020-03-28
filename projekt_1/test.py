import requests
from bs4 import BeautifulSoup

from olx import OLX
from otodom import OTODOM

# otodom = OTODOM('https://www.otodom.pl/sprzedaz/mieszkanie/wroclaw/')
#
# olx = OLX('https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/wroclaw/')
# otodom.create_flats()
# olx.create_flats()
#
# #
# # for k, v in olx.dict_flats.items():
# #     print(f'{k}           {v}')
#
# otodom.save_to_file('otodom')
# olx.save_to_file('olxflats')
#
#
# # for flat in olx.flats:
# #     print(flat.title)
#
# olx.save_to_file('jsonolx')

response = requests.get(
    'https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/wroclaw/')
soup = BeautifulSoup(response.text, 'html.parser')
pages = soup.findAll('span', attrs={'class': 'item fleft'})
print(pages[-1].text.split())
# for page in pages:
#     print(page.text)
# offers_table = soup.find('table', attrs={'id': 'offers_table'})
# dict22 = {}
# for el in offers_table.find_all('tr', attrs={'class': 'wrap'}):
#     data = {}
#     # print('-----')
#     price = el.find('p', attrs={'class': 'price'}).text.strip()
#     print('price: ' + price.strip())
#     data['price'] = price
#     name = el.find('div', attrs={'class': 'space rel'})
#     # print('name: ' + name.find('strong').text)
#     data['name'] = name.find('strong').text
#     link = el.find('a', attrs={'class': 'marginright5 link linkWithHash detailsLink'})
#     if link:
#         data['link'] = link['href']
#         # print(link['href'])
#     link = el.find('a', attrs={'class': 'marginright5 link linkWithHash detailsLinkPromoted'})
#     if link:
#         data['link'] = link['href']
#         # print(link['href'])
#     option = el.find('p', attrs={'class': "offer-path color-9 lheight16 margintop5"})
#     data['option'] = option.text.strip().split(' » ')[1]
#     print(option)
#     print('opcja: ' + option.text.strip().split(' » ')[1])
#     if option == 'Sprzedaż':
#         negotiation = el.find('span', attrs={'class': 'normal inlblk pdingtop5 lheight16 color-2'})
#         if negotiation:
#             data['negotiation'] = negotiation.text
#             # print('negotiation: ' + negotiation.text)
#
#             # print(sp)
#             # print(sp.find(attrs={"data-icon=location-filled" : True}))

    # dict22[data['name']] = data

# for k, v in dict22.items():
#     print(k)
#     for kk, vv in v.items():
#         print(f' {kk}  :  {vv}')



# offers_table._find_all()
# print(offers_table)