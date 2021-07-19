import json

from flask import jsonify, request

from app import app
from app.redsky import RedSkyService
from app.services import MyRetailService

redsky_servie = RedSkyService()
service = MyRetailService(redsky_servie)


@app.route('/')
def index():
    return 'Welcome to myRetail'


@app.route('/products', methods=['GET'])
def get_product():
    products = service.get_product()
    return jsonify([json.loads(product.to_json()) for product in products]), 200


@app.route('/products/<product_id>', methods=['GET'])
def get_product_by_id(product_id):
    product = service.get_product_by_id(product_id)
    return jsonify(json.loads(product.to_json())), 200


@app.route('/products', methods=['POST'])
def create_product():
    record = json.loads(request.data)
    product = service.create_product(product_id=record['product_id'],
                                     product_description=record['product_description'],
                                     current_price=record['current_price'])
    return jsonify([json.loads(product.to_json())]), 201


@app.route('/products/<product_id>', methods=['PUT'])
def modify_product(product_id):
    record = json.loads(request.data)
    product = service.modify_product(product_id=product_id,
                                     product_description=record['product_description'],
                                     current_price=record['current_price'])
    return jsonify(product), 202


@app.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    service.delete_product(product_id)
    response = {'message': f'Product {product_id} is deleted'}
    return jsonify(response)
