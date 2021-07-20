import unittest
from unittest.mock import Mock

from app.exceptions import BadRequestException
from app.models import Product
from app.services import MyRetailService


class TestMethods(unittest.TestCase):

    def setUp(self) -> None:
        Product.objects().delete()

    def test_create_product(self):
        mock_redsky_service = Mock()
        service = MyRetailService(mock_redsky_service)
        actual_value = service.create_product(product_id='1234', product_description='test',

                                              current_price={'value': 12.0,
                                                             'currency_code': 'USD'})
        assert actual_value.product_id == '1234'
        assert actual_value.product_description == 'test'
        assert actual_value.current_price.value == 12.0
        assert actual_value.current_price.currency_code == 'USD'

    def test_create_product_exception(self):
        mock_redsky_service = Mock()
        service = MyRetailService(mock_redsky_service)
        service.create_product(product_id='1234', product_description='test', current_price={'value': 12.0,
                                                                                             'currency_code': 'USD'})

        with self.assertRaises(BadRequestException):
            service.create_product(product_id='1234', product_description='test',
                                   current_price={'value': 12.0,
                                                  'currency_code': 'USD'})

    def test_get_product_by_id(self):
        # data setup
        mock_redsky_service = Mock()
        service = MyRetailService(mock_redsky_service)
        product = Product(product_id='1234', product_description='test', product_name='test',
                          current_price={'value': 12.0, 'currency_code': 'USD'})
        product.save()
        mock_redsky_service.get_product_name.return_value = 'redsky name'

        # calling function under test
        actual_value = service.get_product_by_id('1234')

        # verifying results
        assert actual_value.product_id == '1234'
        assert actual_value.product_description == 'test'
        assert actual_value.product_name == 'redsky name'
        assert actual_value.current_price.value == 12.0
        assert actual_value.current_price.currency_code == 'USD'

    def test_get_product_by_id_exception(self):
        mock_redsky_service = Mock()
        service = MyRetailService(mock_redsky_service)
        with self.assertRaises(BadRequestException):
            service.get_product_by_id('1234')

    def test_modify_product(self):
        mock_redsky_service = Mock()
        service = MyRetailService(mock_redsky_service)
        product = Product(product_id='1234', product_description='test', product_name='test',
                          current_price={'value': 12.0, 'currency_code': 'USD'})
        product.save()
        actual_value = service.modify_product(product_id='1234', product_description='test product',
                                              current_price={'value': 12.78, 'currency_code': 'USD'})

        assert actual_value.product_id == '1234'
        assert actual_value.product_description == 'test product'
        assert actual_value.current_price.value == 12.78
        assert actual_value.current_price.currency_code == 'USD'

    def test_modify_product_exception(self):
        mock_redsky_service = Mock()
        service = MyRetailService(mock_redsky_service)
        with self.assertRaises(BadRequestException):
            service.modify_product(product_id='1234', product_description='test product',
                                   current_price={'value': 12.78, 'currency_code': 'USD'})

    def test_delete_product(self):
        mock_redsky_service = Mock()
        service = MyRetailService(mock_redsky_service)
        product = Product(product_id='1234', product_description='test', product_name='test',
                          current_price={'value': 12.0, 'currency_code': 'USD'})
        product.save()
        service.delete_product('1234')
        actual_value = Product.objects(product_id='1234')

        assert len(actual_value) == 0

    def test_delete_product_exception(self):
        mock_redsky_service = Mock()
        service = MyRetailService(mock_redsky_service)
        with self.assertRaises(BadRequestException):
            service.delete_product('1234')


if __name__ == '__main__':
    unittest.main()

