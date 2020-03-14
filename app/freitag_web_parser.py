import os
import time

import requests
from bs4 import BeautifulSoup

from connect_telegram import telegram_bot


BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
freitag_url = 'https://www.freitag.ch'
freitag_messenger_lassie = freitag_url + '/en/f11'

while True:
    req = requests.get(freitag_messenger_lassie)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    products_div = soup.find(id='products-selector')

    products_path = products_div.get('data-json-path')
    products_url = freitag_url + products_path

    product_list = requests.get(products_url)
    product_json = product_list.json()
    products = product_json['products']

    product_id_list = []
    for product in products:
        product_id = int(product['product']['product_id'])
        product_id_list.append(product_id)
    latest = str(sorted(product_id_list))

    with open(os.path.join(BASE_DIR, 'data/latest.txt'), 'r') as f_read:
        before = f_read.readline()
        if before != latest:
            telegram_bot(message='Update new product')
        else:
            telegram_bot(message='Noting')


    with open(os.path.join(BASE_DIR, 'data/latest.txt'), 'w') as f_write:
        f_write.write(latest)

    time.sleep(60)  # 60sec
