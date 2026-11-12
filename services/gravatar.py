import hashlib
import requests

def gravatar(email):

    email = email.strip().lower()

    hash_value = hashlib.md5(
        email.encode()
    ).hexdigest()

    url = f"https://www.gravatar.com/avatar/{hash_value}?d=404"

    response = requests.get(url)

    if response.status_code == 200:
        return url, True

    return (
        "https://www.gravatar.com/avatar?d=identicon",
        False
    )