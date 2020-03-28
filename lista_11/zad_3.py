import xml.etree.ElementTree as ET


def read_countries(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()
    return [country.get('name') for country in root.findall('country')]


if __name__ == '__main__':
    print(read_countries('kraje.xml'))