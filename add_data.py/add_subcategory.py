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


url = "https://uskunalar.uz.fazliddindehkanoff.uz/admin/api/subcategory/add/"
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

with open("sub-categorys.json") as f:
    sub_categorys = json.load(f)
# The multipart form data should be constructed accordingly
with open("ctg-id.json") as f:
    categorys = json.load(f)

base_url = "https://uskunalar.uz.fazliddindehkanoff.uz"

session = login_to_admin(base_url, "admin", "123")


n = 0
a = 0
for subcategory in sub_categorys:
    category_uz = subcategory["category"]["category_uz"]
    icon_url = subcategory["image"]
    if icon_url:
        icon_filename = icon_url.split("/")[-1]
        icon_path = f"images/{icon_filename}"
        icon_path = download_image(icon_url, icon_path)
    else:
        icon_path = "images/LOGO.png"
    category_id = 0
    for c in categorys:
        if c['title'] == category_uz:
            category_id = c['id']
            break
    if category_id == 0:
        n += 1
        continue
    a += 1
    token = get_csrf_token(session, url)
    print(subcategory['id'])
    multipart_data = {
        "csrfmiddlewaretoken": token,
        "category": str(category_id),
        "title_en": subcategory['subcategory_en'],
        "title_uz": subcategory['subcategory_uz'],
        "title_ru": subcategory['subcategory_ru'],
        "_save": ""
    }
    files = {
        "icon": (icon_filename, open(icon_path, "rb"), "image/png"),
    }
    response = session.post(url, headers=headers, files=files, data=multipart_data)
    print(response.status_code)
    # print(multipart_data)
    # # with open("token.html", "w") as fi:
    # #     fi.write(response.text)
    # if icon_path != "images/LOGO.png":
    #     os.remove(icon_path)
    # break
    # sleep(1)

print(a)
