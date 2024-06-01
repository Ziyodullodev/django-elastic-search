import requests
from adminlogin import login_to_admin, get_csrf_token

base_url = "http://127.0.0.1:8000"

session = login_to_admin(base_url, "ziyodev", "2001")

url = "http://127.0.0.1:8000/admin/api/work/add/"
token = get_csrf_token(session, url)
print(token)
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-CA,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15",
}

# Form data
files = {}
data = {
    "csrfmiddlewaretoken": token,
    "image": (None, ""),
    "view_count": (None, "2"),
    "title_en": (None, "ds"),
    "title_uz": (None, "ds"),
    "title_ru": (None, "sd"),
    "short_description_en": (None, "ds"),
    "id_short_description_en-wmd-wrapper-html-code": (None, "<p>ds</p>"),
    "short_description_uz": (None, ""),
    "id_short_description_uz-wmd-wrapper-html-code": (None, ""),
    "short_description_ru": (None, ""),
    "id_short_description_ru-wmd-wrapper-html-code": (None, ""),
    "long_description_en": (None, ""),
    "id_long_description_en-wmd-wrapper-html-code": (None, ""),
    "long_description_uz": (None, ""),
    "id_long_description_uz-wmd-wrapper-html-code": (None, ""),
    "long_description_ru": (None, ""),
    "id_long_description_ru-wmd-wrapper-html-code": (None, ""),
    "_save": (None, ""),
}

response = session.post(url, headers=headers, files=files, data=data)
with open("work.html", "w") as file:
    file.write(response.text)
# Check response
if response.status_code == 200:
    print("Request successful!")
else:
    print(f"Request failed with status code: {response.status_code}")
