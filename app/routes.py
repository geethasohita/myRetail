from app import app
from app.models import Product, CurrentPrice


@app.route('/')
def index():
    current_price = CurrentPrice(value=12.3, currency_code='USD')
    Product(product_id='1234', product_name='test_product', product_description='test', current_price=current_price).save()
    return 'Welcome to myRetail'
