import requests, json, os
from adminlogin import get_csrf_token, login_to_admin
from time import sleep


def download_image(image_url, save_path):
    response = requests.get(image_url)
    if response.ok:
        with open(save_path, "wb") as file:
            file.write(response.content)
        return save_path
    else:
        # raise Exception(f"Failed to download image from {image_url}")
        return "images/LOGO.png"


url = "https://uskunalar.uz.fazliddindehkanoff.uz/admin/api/product/add/"
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "uz-UZ,uz;q=0.9,en-GB;q=0.8,en;q=0.7,ru-RU;q=0.6,ru;q=0.5,en-US;q=0.4",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "referer": url,
}

with open("data/all-products.json") as f:
    lines = json.load(f)

with open("data/ctg-id.json") as f:
    categorys = json.load(f)

with open("data/sub-categorys-data.json") as f:
    sub_categorys = json.load(f)
# The multipart form data should be constructed accordingly

base_url = "https://uskunalar.uz.fazliddindehkanoff.uz"
#
session = login_to_admin(base_url, "admin", "123")


for data in lines:
    pk_id = data['pk']
    if not os.path.exists(f"products2/{pk_id}.json"):
        continue
    with open(f"products2/{pk_id}.json") as f:
        detail = json.load(f)
    category_title = detail['category']['category_uz']
    sub_category_title = detail['subcategory']['subcategory_uz']
    for category in categorys:
        if category['title'] == category_title:
            category_id = category['id']
            break

    for sub_category in sub_categorys:
        if sub_category['title'] == sub_category_title:
            sub_category_id = sub_category['id']
            break
    token = get_csrf_token(session, url)
    cip_type = 1
    if detail['CIP']:
        cip_type = 1
    elif detail['DAF']:
        cip_type = 1
    elif detail['FCA']:
        cip_type = 3
    elif detail['EXW']:
        cip_type = 2
    multipart_data = {
        "csrfmiddlewaretoken": token,
        "name_en": detail['title_en'],
        "name_uz": detail['title_uz'],
        "name_ru": detail['title_ru'],
        "short_description_en": detail['short_description_en'],
        "id_description_en-wmd-wrapper-html-code": detail['long_description_en'],
        "short_description_uz": detail['short_description_uz'],
        "id_description_uz-wmd-wrapper-html-code": detail['long_description_uz'],
        "short_description_ru": detail['short_description_ru'],
        "id_description_ru-wmd-wrapper-html-code": detail['long_description_ru'],
        "description_en": detail['long_description_en'],
        "description_uz": detail['long_description_uz'],
        "description_ru": detail['long_description_ru'],
        "price": detail['price'],
        "min_price": 0,
        "max_price": 0,
        "approved": "on",
        "discount": detail['discount'],
        "view_count": detail['view_count'],
        "cip_type": cip_type,
        "category": category_id,
        "subcategory": sub_category_id,
        "related_products": [],
        "tags": "non",
        "created_by": 1,
        "background_image": 1,
        "availability_status": 1,
        "supplier": 2,
        "specifications-TOTAL_FORMS": "1",
        "specifications-INITIAL_FORMS": "0",
        "specifications-MIN_NUM_FORMS": "0",
        "specifications-MAX_NUM_FORMS": "1000",
        "specifications-0-title_en": "",
        "specifications-0-title_uz": "",
        "specifications-0-title_ru": "",
        "specifications-0-value_en": "",
        "specifications-0-value_uz": "",
        "specifications-0-value_ru": "",
        "specifications-__prefix__-title_en": "",
        "specifications-__prefix__-title_uz": "",
        "specifications-__prefix__-title_ru": "",
        "specifications-__prefix__-value_en": "",
        "specifications-__prefix__-value_uz": "",
        "specifications-__prefix__-value_ru": "",
        "images-TOTAL_FORMS": "1",
        "images-INITIAL_FORMS": "0",
        "images-MIN_NUM_FORMS": "0",
        "images-MAX_NUM_FORMS": "1000",
        # "images-0-image": ("", open("", "rb"), "application/octet-stream"),
        # "images-__prefix__-image": ("", open("", "rb"), "application/octet-stream"),
        "_save": ""
    }

    # files = {
    #     "image": open(download_image(data['image'], "images/" + data['image'].split("/")[-1]), "rb"),
    #     "banner": open(download_image(data['banner'], "images/" + data['banner'].split("/")[-1]), "rb")
    # }
    # print(multipart_data)
    response = session.post(url, headers=headers, data=multipart_data)
    # with open("log.html", "w") as f:
    #     f.write(response.text)
    print(response.status_code, pk_id)
#     # print(multipart_data)
    # break
    sleep(1)


# 200 1167