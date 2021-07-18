import os

from flask import Flask
from flask_mongoengine import MongoEngine
from mongoengine import connect

app = Flask(__name__)

db_url = os.environ.get('DATABASE_URI', None)
if not db_url:
    app.config['MONGODB_SETTINGS'] = {
        'db': 'myretail',
        'host': 'localhost',
        'port': 27017
    }
else:
    connect(host=db_url, alias="myretail")

db = MongoEngine()
db.init_app(app)

from app import routes, models
