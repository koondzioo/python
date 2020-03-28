import json


def print_countries(file_name):
    """Function to print countries from json file"""
    with open(file_name) as json_file:
        json_data = json.load(json_file)
        return [element['name'] for element in json_data['products']]


if __name__ == '__main__':
    print(print_countries('kraje.json'))