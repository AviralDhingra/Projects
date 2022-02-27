"""ARCHIVE ---- OLDER CODE (backup) v1"""


import sys

import requests
from bs4 import BeautifulSoup

# sys.argv


def getAmazonPrice(productUrl):
    # res = requests.get(productUrl)
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
    print("[+] Selection...")
    # elem = soup.selector(
    #     'Jump right in')
    elem = soup.select('#priceblock_ourprice')

    try:
        return elem[0].text.strip()  # Succesfull
    except IndexError:
        return elem  # (List Index Out Of Range) Failed Try, Again


price = []  # Definign Before Function Is Actually Called
while price == []:
    print()
    price = getAmazonPrice('https://www.amazon.in/dp/B087JWLZ2K/ref=s9_acsd_al_bw_c2_x_1_i?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-5&pf_rd_r=3FZHC0FVKBK77QYMJ0DQ&pf_rd_t=101&pf_rd_p=50675d9d-029a-42f0-8c73-fd7fe76f10f1&pf_rd_i=22817284031')
    v = list(price)
    print('[+] Pinging')
    print(price)
    print(type(price))

    print(v)
    print(type(v))


print()
print()

finalPrice = " ".join(v)  # v[0] + v[1] + v[2] ...
finalPrice = finalPrice.strip()
finalPrice = finalPrice.replace(" ", "")
print(finalPrice)
# if price == False:
#     # print(price)
#     pass
# else:
#     print(f'The Price is ${price}')
