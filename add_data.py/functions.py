from adminlogin import get_csrf_token
import requests


def download_image(image_url, save_path):
    response = requests.get(image_url)
    if response.ok:
        with open(save_path, "wb") as file:
            file.write(response.content)
    else:
        raise Exception(f"Failed to download image from {image_url}")


def add_category(session, base_url, title_en, title_uz, title_ru, icon_path):

    # Step 1: Get CSRF token
    add_url = f"{base_url}/admin/api/category/add/"
    csrf_token = get_csrf_token(session, add_url)

    # Step 2: Send POST request to add a new category
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
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "referer": add_url,
    }

    # Multipart form data
    files = {
        "csrfmiddlewaretoken": (None, csrf_token),
        "icon": (
            icon_path,
            open(icon_path, "rb"),
            "image/png",
        ),  # Adjust MIME type as needed
        "title_en": (None, title_en),
        "title_uz": (None, title_uz),
        "title_ru": (None, title_ru),
        "_save": (None, ""),
    }

    response = session.post(add_url, headers=headers, files=files)

    return response.status_code, response.text


def add_work(
    session,
    base_url,
    title_en,
    title_uz,
    title_ru,
    icon_url,
    short_descriptions,
    short_descriptions_uz,
    short_descriptions_ru,
    short_descriptions_en,
    descriptions,
    descriptions_uz,
    descriptions_ru,
    descriptions_en,
    views,
    created_at,
):
    # Step 1: Get CSRF token
    add_url = f"{base_url}/admin/api/category/add/"
    csrf_token = get_csrf_token(session, add_url)

    # Step 2: Download the image
    icon_filename = icon_url.split("/")[-1]
    icon_path = f"images/{icon_filename}"
    download_image(icon_url, icon_path)

    # Step 3: Submit the form data with the image
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
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "referer": add_url,
    }

    files = {
        "csrfmiddlewaretoken": (None, csrf_token),
        "icon": (
            icon_filename,
            open(icon_path, "rb"),
            "image/png",
        ),  # Adjust MIME type as needed
        "title_en": (None, title_en),
        "title_uz": (None, title_uz),
        "title_ru": (None, title_ru),
        "short_descriptions": (None, short_descriptions),
        "short_descriptions_uz": (None, short_descriptions_uz),
        "short_descriptions_ru": (None, short_descriptions_ru),
        "short_descriptions_en": (None, short_descriptions_en),
        "descriptions": (None, descriptions),
        "descriptions_uz": (None, descriptions_uz),
        "descriptions_ru": (None, descriptions_ru),
        "descriptions_en": (None, descriptions_en),
        "views": (None, str(views)),
        "created_at": (None, created_at),
        "_save": (None, ""),
    }

    response = session.post(add_url, headers=headers, files=files)

    return response.status_code, response.text
