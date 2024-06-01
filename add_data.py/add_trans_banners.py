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


url = "https://uskunalar.uz.fazliddindehkanoff.uz/admin/api/video/add/"
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

with open("data/videoes.json") as f:
    lines = json.load(f)


# The multipart form data should be constructed accordingly

base_url = "https://uskunalar.uz.fazliddindehkanoff.uz"

session = login_to_admin(base_url, "admin", "123")

for data in lines:
    token = get_csrf_token(session, url)
    if data['description_uz'] == "":
        data['description_uz'] = "non"
    if data['description_ru'] == "":
        data['description_ru'] = "non"
    if data['description_en'] == "":
        data['description_en'] = "non"
    multipart_data = {
        "csrfmiddlewaretoken": token,
        "title_en": data['title_en'],
        "title_uz": data['title_uz'],
        "title_ru": data['title_ru'],
        "description_en": data['description_en'],
        "description_uz": data['description_uz'],
        "description_ru": data['description_ru'],
        "video_link": data['url'],
        "_save": ""
    }

    response = session.post(url, headers=headers, data=multipart_data)
    # with open("log.html", "w") as f:
    #     f.write(response.text)
    print(response.status_code)
#     # print(multipart_data)
    # break
    # sleep(1)

# print(l)