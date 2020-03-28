import random


def convert_fahrenheit_to_celsius(fahrenheit):
    """Function to convert fahrenheit to celsius"""
    return round((fahrenheit - 32) * (5 / 9), 2)


def convert_celsius_to_fahrenheit(celsius):
    """Function to convert celsius to fahrenheit"""
    return round(celsius * (9 / 5) + 32, 2)


def generate_random_temperature():
    return random.randint(-50, 50)

