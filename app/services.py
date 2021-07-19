from app.models import Product
from app.exceptions import BadRequestException
from app.redsky import RedSkyService


class MyRetailService:

    def __init__(self, redsky_service):
        self.redsky_service = redsky_service

    def get_product(self):
        products = Product.objects.exclude('id')
        for product in products:
            redsky_product_name = self.redsky_service.get_product_name(product.product_id)
            product.product_name = redsky_product_name
        return products

    def get_product_by_id(self, product_id):
        product = Product.objects.exclude('id')(product_id=product_id).first()
        if product is None:
            raise BadRequestException(f'Product with id {product_id} does not exist in database.')
        redsky_product_name = self.redsky_service.get_product_name(product_id)
        product.product_name = redsky_product_name

        return product

    def create_product(self, product_id, product_description, current_price):
        product = Product(product_id=product_id, product_name=None,
                          product_description=product_description, current_price=current_price)
        existing_product = Product.objects(product_id=product_id).first()
        if existing_product:
            raise BadRequestException(f'Product with id {product_id} already exists in database.')
        product.save()
        return product

    def modify_product(self, product_id, product_description, current_price):
        product = Product.objects(product_id=product_id).first()
        if not product:
            raise BadRequestException(f'Product with id {product_id} does not exist in database.')
        product.modify(product_id=product_id, product_description=product_description, current_price=current_price)
        return product

    def delete_product(self, product_id):
        product = Product.objects(product_id=product_id).first()
        if not product:
            raise BadRequestException(f'Product with id {product_id} does not exist in database.')
        product.delete()
