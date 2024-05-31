import json
import requests, os
from bs4 import BeautifulSoup
from adminlogin import login_to_admin

def get_csrf_token(session, url):
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
    return csrf_token

def download_image(image_url, save_path):
    response = requests.get(image_url)
    if response.ok:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        return save_path
    else:
        # raise Exception(f"Failed to download image from {image_url}")
        return "images/LOGO.png"

def add_work(session, base_url, title_en, title_uz, title_ru, icon_url,
            short_descriptions_uz = "test", short_descriptions_ru= "test", short_descriptions_en="test",
            descriptions_uz= "test", descriptions_ru= "test", descriptions_en= "test", views=0, created_at=0):
    # Step 1: Get CSRF token
    add_url = f"{base_url}/admin/api/work/add/"
    csrf_token = get_csrf_token(session, add_url)
    if not short_descriptions_uz:
        short_descriptions_uz = "non"
    if not short_descriptions_ru:
        short_descriptions_ru = "non"
    if not short_descriptions_en:
        short_descriptions_en = "non"
    if not descriptions_uz:
        descriptions_uz = "non"
    if not descriptions_ru:
        descriptions_ru = "non"
    if not descriptions_en:
        descriptions_en = "non"
    # Step 2: Download the image
    icon_filename = icon_url.split("/")[-1]
    icon_path = f"images/{icon_filename}"
    icon_path = download_image(icon_url, icon_path)

    # Step 3: Submit the form data with the image
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "uz-UZ,uz;q=0.9,en-GB;q=0.8,en;q=0.7,ru-RU;q=0.6,ru;q=0.5,en-US;q=0.4",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "referer": add_url,
    }
    
    files = {
        "csrfmiddlewaretoken": (None, csrf_token),
        "image": (icon_filename, open(icon_path, 'rb'), 'image/png'),  # Adjust MIME type as needed
        "title_en": (None, title_en),
        "title_uz": (None, title_uz),
        "title_ru": (None, title_ru),
        "short_description_en": (None, short_descriptions_en),
        "id_short_description_en-wmd-wrapper-html-code": (None, short_descriptions_en),
        "short_description_uz": (None, short_descriptions_uz),
        "id_short_description_uz-wmd-wrapper-html-code": (None, short_descriptions_uz),
        "short_description_ru": (None, short_descriptions_ru),
        "id_short_description_ru-wmd-wrapper-html-code": (None, short_descriptions_ru),
        "long_description_en": (None, descriptions_en),
        "id_long_description_en-wmd-wrapper-html-code": (None, descriptions_en),
        "long_description_uz": (None, descriptions_uz),
        "id_long_description_uz-wmd-wrapper-html-code": (None, descriptions_uz),
        "long_description_ru": (None, descriptions_ru),
        "id_long_description_ru-wmd-wrapper-html-code": (None, descriptions_ru),
        "view_count": (None, str(views)),
        # "created_at": (None, created_at),
        "_save": (None, "")
    }
    response = session.post(add_url, headers=headers, files=files)
    if icon_path != "images/LOGO.png":
        os.remove(icon_path)
    return response.status_code, response.text

# Example usage
with open('works.json') as f:
    datas = json.load(f)

base_url = "http://127.0.0.1:8000"
base_url = "https://uskunalar.uz.fazliddindehkanoff.uz"
username = "admin"
password = "123"

session = login_to_admin(base_url, username, password)
for data in datas:
    title_en = data['title_en']
    title_uz = data['title_uz']
    title_ru = data['title_ru']
    icon_url = data['image']
    short_descriptions = data['short_descriptions']
    short_descriptions_uz = data['short_descriptions_uz']
    short_descriptions_ru = data['short_descriptions_ru']
    short_descriptions_en = data['short_descriptions_en']
    descriptions = data['descriptions']
    descriptions_uz = data['descriptions_uz']
    descriptions_ru = data['descriptions_ru']
    descriptions_en = data['descriptions_en']
    views = data['views']
    created_at = data['created_at']
    
    status_code, response_text = add_work(
        session, base_url, title_en, title_uz, title_ru, icon_url,
        short_descriptions_uz, short_descriptions_ru, short_descriptions_en,
        descriptions_uz, descriptions_ru, descriptions_en, views, created_at
    )
    print(f"Status code: {status_code}")
    # with open("work.html", "w") as file:
    #     file.write(response_text)
    # break
    # print(f"Response: {response_text}")
