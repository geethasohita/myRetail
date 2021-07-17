import json

from flask import jsonify

from app import app
from app.models import Product


@app.route('/')
def index():
    return 'Welcome to myRetail'


@app.route('/product', methods=['GET'])
def get_product():
    products = Product.objects()
    return jsonify([json.loads(product.to_json()) for product in products])