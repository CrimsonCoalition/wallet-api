# Imports / Импорты

import requests # Импортируем библиотеку request - "запросы", понятно для чего)
import flask
from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
app = Flask(__name__)
api = Api(app)

url = 'http://pay.crimsoncoalition.cc'
