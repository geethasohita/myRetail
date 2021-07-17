import json

from flask import jsonify, request

from app import app
from app.models import Product


@app.route('/')
def index():
    return 'Welcome to myRetail'


@app.route('/product', methods=['GET'])
def get_product():
    products = Product.objects.exclude('id')
    return jsonify([json.loads(product.to_json()) for product in products])


@app.route('/product', methods=['POST'])
def create_product():
    record = json.loads(request.data)
    product = Product(product_id=record['product_id'], product_name=record['product_name'],
                      product_description=record['product_description'], current_price=record['current_price'])
    product.save()
    return jsonify([json.loads(product.to_json())])
