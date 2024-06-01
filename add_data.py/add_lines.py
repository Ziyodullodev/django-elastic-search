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


url = "https://uskunalar.uz.fazliddindehkanoff.uz/admin/api/line/add/"
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

with open("data/lines.json") as f:
    lines = json.load(f)

with open("data/lines-category2.json") as f:
    sub_categorys = json.load(f)
# The multipart form data should be constructed accordingly
categorys = sub_categorys['results']
# The multipart form data should be constructed accordingly

base_url = "https://uskunalar.uz.fazliddindehkanoff.uz"
#
session = login_to_admin(base_url, "admin", "123")

l = 0
ruxsat = [7,13,18,19,21,22,23,25,27,29,30,31,32,40,42]
for data in lines:
    l += 1
    if l not in ruxsat:
        continue
    data_category_id = data['category']['id']
    for category in categorys:
        if category['id'] == data_category_id:
            category_id = category['id2']
            break
    token = get_csrf_token(session, url)
    print(l)
    multipart_data = {
        "csrfmiddlewaretoken": token,
        "title_en": data['title_en'],
        "title_uz": data['title_uz'],
        "title_ru": data['title_ru'],
        "short_description_en": data['description_en'],
        "short_description_uz": data['description_uz'],
        "short_description_ru": data['description_ru'],
        "long_description_en": data['long_description_en'],
        "long_description_uz": data['long_description_uz'],
        "long_description_ru": data['long_description_ru'],
        "price": data['price'],
        "view_count": data['views'],
        "category": category_id,
        "_save": ""
    }

    files = {
        "image": open(download_image(data['image'], "images/" + data['image'].split("/")[-1]), "rb"),
        "banner": open(download_image(data['banner'], "images/" + data['banner'].split("/")[-1]), "rb")
    }
    print(multipart_data)
    response = session.post(url, headers=headers, data=multipart_data, files=files)
    with open("data/lines-category2.html", "w") as f:
        f.write(response.text)
    print(response.status_code)
#     # print(multipart_data)
    break
    # sleep(1)

print(l)