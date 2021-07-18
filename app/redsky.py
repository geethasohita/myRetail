import json

import requests


class RedSkyService:
    def get_product_name(self, product_id):
        product_name = 'Name not available in redsky'
        try:
            url = f'https://redsky.target.com/v3/pdp/tcin/{product_id}?key=candidate'
            response = requests.get(url)
            json_data = json.loads(response.text)
            product_name = json_data['product']['item']['product_description']['title']
        except Exception as error:
            print('Error in getting product name')
        return product_name
