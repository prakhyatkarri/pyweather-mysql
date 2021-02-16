import json

from flask import Flask

import service.service
from repo import db

app = Flask(__name__)


@app.route('/')
def home():
    result = db.get_all_records()
    data = json.dumps(result)
    return 'Welcome to this Page! \n \n' + data


@app.route('/load')
def load():
    return service.service.load()


@app.route('/weather')
def weather():
    return service.service.get_weather()


@app.route('/weather/<city_name>')
def city_weather(city_name):
    return service.service.get_city_weather(city_name)


if __name__ == '__main__':
    app.run()
