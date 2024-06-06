import requests, json, os
from adminlogin import get_csrf_token, login_to_admin
from time import sleep


base_url = "https://student.fbtult.uz"
#
session = login_to_admin(base_url, "ziyodev", "2001")


url = "http://student.fbtult.uz/admin/fbtuit/examsemesterquestion/"
params = {
    "q": "Qutida 5 ta bir xil buyum bo‘lib, ularning 3 tasi bo‘yalgan. Tavakkaliga 2 ta buyum olinganda ular orasida 2 ta bo‘yalgan bo‘lishi ehtimolligini toping."
}
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-CA,en-US;q=0.9,en;q=0.8",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15"
}

response = session.get(url, headers=headers, params=params)

print(response.status_code)
with open("token.html", "w") as f:
    f.write(response.text)