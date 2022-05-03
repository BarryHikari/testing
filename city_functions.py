from logging import NullHandler


def city_country(city, country, population=None):
    full_info = f'{city}, {country} - populacja {population}'
    return full_info