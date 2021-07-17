from app.models import Product


class MyRetailService:

    def get_product(self):
        products = Product.objects.exclude('id')
        return products

    def get_product_by_id(self, product_id):
        product = Product.objects.exclude('id')(product_id=product_id).first()
        return product

    def create_product(self, product_id, product_name, product_description, current_price):
        product = Product(product_id=product_id, product_name=product_name,
                          product_description=product_description, current_price=current_price)
        product.save()
        return product

    def modify_product(self, product_id, product_name, product_description, current_price):
        product = Product.objects(product_id=product_id).first()
        product.modify(product_name=product_name, product_description=product_description, current_price=current_price)
        return product

    def delete_product(self, product_id):
        product = Product.objects(product_id=product_id).first()
        product.delete()
        return product

