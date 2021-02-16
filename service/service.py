import json

import requests

from models.city import City
from repo import db


def read_from_file():
    file_path = 'data/cities.json'

    try:
        with open(file_path) as file:
            cities = json.load(file)
    except Exception as e:
        print(f'Exception in load() : {e}')
    finally:
        file.close()
    return cities


def load():
    cities = read_from_file();

    city_list = get_cities(cities)

    for city in city_list: db.insert_city(city)

    return json.dumps([ct.__dict__ for ct in city_list])


def get_cities(cities):
    city_list = []

    if cities is None or len(cities) == 0:
        return city_list

    for line in cities:
        city = City(line['city'], line['state'])
        city_list.append(city)

    return city_list


def get_weather():
    cities = read_from_file()
    city_weather = get_weather_for_city(cities[0]['city'])
    return city_weather.json()


def get_city_weather(city_name):
    if city_name is None or len(city_name) == 0:
        return ''

    return get_weather_for_city(city_name).json()


def get_weather_for_city(city_name):
    secrets = get_secrets()
    url = secrets['url']
    api_key = secrets['api-key']

    formatted_url = url.format(city_name=city_name, api_key=api_key)

    response = requests.get(formatted_url)

    return response


def get_secrets():
    secret_file_path = 'config/secrets.json'

    try:
        with open(secret_file_path) as sf:
            return json.load(sf)
    except Exception as e:
        print(f'Exception in get_secrets: {e}')
    finally:
        sf.close()

