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


url = "https://uskunalar.uz.fazliddindehkanoff.uz/admin/api/linecategory/add/"
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

with open("data/lines-category.json") as f:
    sub_categorys = json.load(f)
# The multipart form data should be constructed accordingly
categorys = sub_categorys['results']
# base_url = "https://uskunalar.uz.fazliddindehkanoff.uz"

# session = login_to_admin(base_url, "admin", "123")

id2 = 1
for data in categorys:
    id2 += 1
    data['id2'] = id2
    print(data['id2'])

    # token = get_csrf_token(session, url)
    # multipart_data = {
    #     "csrfmiddlewaretoken": token,
    #     "title_en": data['category_en'],
    #     "title_uz": data['category_uz'],
    #     "title_ru": data['category_ru'],
    #     "_save": ""
    # }
    # response = session.post(url, headers=headers, data=multipart_data)
    # print(response.status_code)
#     # print(multipart_data)
    # break
#     # sleep(1)


with open("data/lines-category2.json", "w") as f:
    json.dump(sub_categorys, f, indent=4, ensure_ascii=False)
