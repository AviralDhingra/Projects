import json
import os
from pprint import pprint

import requests
from bs4 import BeautifulSoup


def fetch_raw_definition(productUrl):
    res = requests.get(productUrl, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"
    })
    print(f'Connection Status: {res.status_code}')
    try:
        res.raise_for_status()
    except requests.exceptions.HTTPError:
        print("Invlaid URL...")
        return False

    soup = BeautifulSoup(res.text, 'html.parser')
    soup = str(soup)[1:-1]
    soup = json.loads(soup)
    # elem = soup.select('#priceblock_ourprice')
    inp = input()
    os.system('clear')
    pprint(soup)
    print(type(soup))
    # print(soup['meanings']['definitions']['definition'])
    # print(soup['meanings']['definitions']['example'])
    return True


fetch_raw_definition('https://api.dictionaryapi.dev/api/v2/entries/en/hello')
