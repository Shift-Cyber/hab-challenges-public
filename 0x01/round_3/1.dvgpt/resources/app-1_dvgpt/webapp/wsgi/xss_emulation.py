import os
from urllib.parse import urlparse

def make_xss_request(url, message):
    parsed_url = urlparse(url)

    target_url = f"http://192.168.1.65:5000/{parsed_url.path + parsed_url.query + parsed_url.fragment}"
    print(target_url)

    with open('../xss/target_url.txt', 'w') as fio:
        fio.write(target_url)
