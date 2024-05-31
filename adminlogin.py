import requests
from bs4 import BeautifulSoup


def get_csrf_token(session, login_url):
    # Step 1: Make a GET request to the login page
    response = session.get(login_url)
    # Step 2: Parse the HTML to extract the CSRF token
    soup = BeautifulSoup(response.text, "html.parser")
    csrf_token = soup.find("input", {"name": "csrfmiddlewaretoken"})["value"]
    return csrf_token


def login_to_admin(base_url, username, password):
    login_url = f"{base_url}/admin/login/?next=/admin/"

    # Create a session to persist cookies
    session = requests.Session()

    # Get CSRF token
    csrf_token = get_csrf_token(session, login_url)

    # Step 3: Use the extracted CSRF token to login
    login_data = {
        "csrfmiddlewaretoken": csrf_token,
        "username": username,
        "password": password,
        "next": "/admin/",
    }

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
        "referer": login_url,
    }

    # Perform the login POST request
    session.post(login_url, data=login_data, headers=headers)

    return session
