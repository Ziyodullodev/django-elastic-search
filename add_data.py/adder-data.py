from adminlogin import login_to_admin, get_csrf_token
import requests
from bs4 import BeautifulSoup



# Example usage:
# base_url = "https://uskunalar.uz.fazliddindehkanoff.uz"
base_url = "http://127.0.0.1:8000"
username = "admin"
password = "123"

# session = login_to_admin(base_url, username, password)

# # Example usage:
# category qoshish
# status_code, response_text = add_category(session, base_url, title_en, title_uz, title_ru, icon_path)

import json

with open('categorys.json') as f:
    categorys = json.load(f)

with open('ctg-id.json') as f:
    categorys_id = json.load(f)

for category in categorys:
    category_uz = category['category_uz']
    for ctg_id in categorys_id:
        if ctg_id['title'] == category_uz:
            category['ids'] = ctg_id['id']
    # print(category['ids'])

with open('categorys.json', "w") as f:
    categorys = json.dumps(categorys)