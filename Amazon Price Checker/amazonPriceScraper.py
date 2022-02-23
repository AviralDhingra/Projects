import sys

import requests
from bs4 import BeautifulSoup

# NOTE Features + Real Time Updateing (Backend...) (Helpful Things)
# TODO MultiThreading : check multiple sites simultaneously, add a database of products to check
# TODO Baground process (while loop keeps on running)
# TODO Remove CSS Selectors, Program WIll FInd Price On Its Own

# NOTE UI/UX
# TODO Add "sys.argv" for link, css selector, type of email, range, etc. (Accept user Input)
# TODO Add A UI : Website or Application (Not tkinter)

# NOTE Shipment (Of App)
# TODO Better explaination & Update (According To Chnages) In "readme.txt"

# NOTE Done Tasks ** Updated
# TODO Sort comments & extra code for all files $$$$$ DONE


def getAmazonPrice(productUrl):
    res = requests.get(productUrl, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"
    })
    # print(f'Connection Status: {res.status_code}')
    try:
        res.raise_for_status()
    except requests.exceptions.HTTPError:
        print("Invlaid URL...")
        return False

    soup = BeautifulSoup(res.text, 'html.parser')
    elem = soup.select('#priceblock_ourprice')

    try:
        return elem[0].text.strip()  # Succesfull
    except IndexError:
        return elem  # (List Index Out Of Range) Failed Try, Again


# price = []  # Definign Before Function Is Actually Called
# while price == []:
#     # print()
#     price = getAmazonPrice('https://www.amazon.in/dp/B087JWLZ2K/ref=s9_acsd_al_bw_c2_x_1_i?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-5&pf_rd_r=3FZHC0FVKBK77QYMJ0DQ&pf_rd_t=101&pf_rd_p=50675d9d-029a-42f0-8c73-fd7fe76f10f1&pf_rd_i=22817284031')
#     v = list(price)
#     # print('[+] Pinging')
#     # print(price)
#     # print(type(price))

#     # print(v)
#     # print(type(v))


# # print()
# # print()

# finalPrice = " ".join(v)  # v[0] + v[1] + v[2] ...
# finalPrice = finalPrice.strip()
# finalPrice = finalPrice.replace(" ", "")
# finalPrice = finalPrice.replace("₹", "")
# finalPrice = finalPrice.replace(",", "")
# finalPrice = float(finalPrice)
# idealPrice = float(28999)


# status = priceChnageChecker(idealPrice, finalPrice)

# print(finalPrice)


# if price == False:
#     # print(price)
#     pass
# else:
#     print(f'The Price is ${price}')
