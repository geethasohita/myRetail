from app.models import Product
from app.exceptions import BadRequestException


class MyRetailService:

    def get_product(self):
        products = Product.objects.exclude('id')
        return products

    def get_product_by_id(self, product_id):
        product = Product.objects.exclude('id')(product_id=product_id)
        return product

    def create_product(self, product_id, product_name, product_description, current_price):
        product = Product(product_id=product_id, product_name=product_name,
                          product_description=product_description, current_price=current_price)
        existing_product = self.get_product_by_id(product_id)
        if len(existing_product) > 0:
            raise BadRequestException(f'Product with id {product_id} already exists in database.')
        product.save()
        return product

    def modify_product(self, product_id, product_name, product_description, current_price):
        product = self.get_product_by_id(product_id=product_id)
        if not product:
            raise BadRequestException(f'Product with id {product_id} does not exist in database.')
        product.modify(product_name=product_name, product_description=product_description, current_price=current_price)
        return product

    def delete_product(self, product_id):
        product = self.get_product_by_id(product_id=product_id)
        if not product:
            raise BadRequestException(f'Product with id {product_id} does not exist in database.')
        product.delete()

