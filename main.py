import requests
import random
from captcha_solver import CaptchaSolver

solver = CaptchaSolver('twocaptcha', api_key='2captcha.com API HERE')


def register(email, username):
    password = ""
    for index in range(12):
        password = password + random.choice("abcde12345")

    s = requests.Session()
    payload = {
        "email": email,
        "username": username,
        "password": password,
        "date_of_birth": "1991-01-01",
        "captcha_key:": solver,
        "consent": True,
        "fingerprint": "1012769912755863703.5Su4sT3GZnKDira1UdfJfMYAZ9o"
    }

    res = s.post("https://discord.com/api/v9/auth/register", json=payload)
    print(res.content)

    return s


session = register("sdosefsef@gmail.com", "dsffqwoqwo")