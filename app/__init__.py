import os

from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)

db_uri = os.environ.get('DATABASE_URI', None)
if not db_uri:
    db_uri = 'mongomock://localhost'
app.config['MONGODB_SETTINGS'] = {
    'host': db_uri
}
db = MongoEngine(app)

from app import routes, models
