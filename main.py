import os
import json
import requests
from time import sleep

with open('all-products.json') as f:
    products = json.load(f)


for product in products:
    product_id = product['pk']
    if product_id < 75:
        url = f"https://api.uskunalar.uz/en/api-auth/products/{product_id}"
        data = requests.get(url)
        with open(f'products2/{product_id}.json', 'w') as f:
            f.write(data.text)
        print(f"Product {product_id} is saved")
        sleep(1)
