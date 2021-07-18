import json

from flask import jsonify, request

from app import app
from app.services import MyRetailService

service = MyRetailService()

@app.route('/')
def index():
    return 'Welcome to myRetail'


@app.route('/product', methods=['GET'])
def get_product():
    products = service.get_product()
    return jsonify([json.loads(product.to_json()) for product in products]), 200


@app.route('/product/<product_id>', methods=['GET'])
def get_product_by_id(product_id):
    product = service.get_product_by_id(product_id)
    return jsonify([json.loads(product.to_json())]), 200


@app.route('/product', methods=['POST'])
def create_product():
    record = json.loads(request.data)
    product = service.create_product(product_id=record['product_id'], product_name=record['product_name'],
                                     product_description=record['product_description'],
                                     current_price=record['current_price'])
    return jsonify([json.loads(product.to_json())]), 201


@app.route('/product/<product_id>', methods=['PUT'])
def modify_product(product_id):
    record = json.loads(request.data)
    product = service.modify_product(product_id=product_id, product_name=record['product_name'],
                                     product_description=record['product_description'],
                                     current_price=record['current_price'])
    return jsonify(product), 202


@app.route('/product/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = service.delete_product(product_id)
    return jsonify(product), 202
