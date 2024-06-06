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


url = "https://uskunalar.uz.fazliddindehkanoff.uz/admin/api/productfeature/add/"
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

# with open("data/all-products.json") as f:
    # lines = json.load(f)

with open("data/all-products.json") as f:
    products = json.load(f)

with open("products.json") as f:
    products_base = json.load(f)
# The multipart form data should be constructed accordingly

base_url = "https://uskunalar.uz.fazliddindehkanoff.uz"
#
session = login_to_admin(base_url, "admin", "123")

ishla = False
for data in products:
    pk_id = data['pk']
    if not os.path.exists(f"products2/{pk_id}.json"):
        continue
    with open(f"products2/{pk_id}.json") as f:
        detail = json.load(f)
    # detail['product_id'] = pk_id
    # bor = False
    # for pr in products_base:
    #     if pr['fields']['name_ru'] == detail['title_ru']:
    #         # print(pr['pk'])
    #         # print(pr['fields']['name_uz'])
    #         bor = True
    #         break
    # if bor:
    #     detail['product_id'] = pr['pk']
    # else:
    #     detail['product_id'] = "no"
    #     print("yoq")
    # with open(f"products2/{pk_id}.json", "w") as f:
    #     json.dump(detail, f)

    if detail['product_id'] == "no":
        continue
    if detail["product_id"] == 857:
        ishla = True
    if not ishla:
        continue 1276
    print(detail["product_id"])
    features = detail['specifications']
    for f in features:
        token = get_csrf_token(session, url)
        multipart_data = {
            "csrfmiddlewaretoken": token,
            "title_en": f['product_customer_en'],
            "title_uz": f['product_customer_uz'],
            "title_ru": f['product_customer_ru'],
            "value_uz": f['product_number_uz'],
            "value_ru": f['product_number_ru'],
            "value_en": f['product_number_en'],
            "product": detail['product_id'],
            "_save": ""
        }
        response = session.post(url, headers=headers, data=multipart_data)
        # with open("token.html", "w") as f:
        #     f.write(response.text)
        if response.status_code != 200:
            print(response.status_code, pk_id)
            print(multipart_data)
        sleep(1)
    #     break
    # break
    # files = {
    #     "image": open(download_image(data['image'], "images/" + data['image'].split("/")[-1]), "rb"),
    #     "banner": open(download_image(data['banner'], "images/" + data['banner'].split("/")[-1]), "rb")
    # }
    # print(multipart_data)
    # response = session.post(url, headers=headers, data=multipart_data)
#     # with open("log.html", "w") as f:
#     #     f.write(response.text)
#     print(response.status_code, pk_id)
# #     # print(multipart_data)
#     # break
    


# # 200 1167