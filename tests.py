import os
import unittest
from unittest import mock
from unittest.mock import Mock

from flask_mongoengine import MongoEngine

from app import app
from test.support import EnvironmentVarGuard

from app.exceptions import BadRequestException
from app.services import MyRetailService


class TestMethods(unittest.TestCase):

    def test_create_product(self):
        service = MyRetailService()
        actual_value = service.create_product(product_id='1234', product_description='test',
                                              current_price={'value': 12.0,
                                                             'currency_code': 'USD'})
        assert actual_value.product_id == '1234'
        assert actual_value.product_description == 'test'
        assert actual_value.current_price.value == 12.0
        assert actual_value.current_price.currency_code == 'USD'

    def test_create_product_exception(self):
        service = MyRetailService()
        service.create_product(product_id='1235', product_description='test', current_price={'value': 12.0,
                                                                                             'currency_code': 'USD'})

        with self.assertRaises(BadRequestException):
            service.create_product(product_id='1235', product_description='test',
                                   current_price={'value': 12.0,
                                                  'currency_code': 'USD'})


