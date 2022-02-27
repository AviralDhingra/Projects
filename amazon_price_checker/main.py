import os

# import notify2
from mailer import Mailer

from amazonPriceScraper import getAmazonPrice

# NOTE Getting The Price... getAmazonPrice + Strign FIltering + IdealPrice


def getPriceUpdate(idealPrice):

    price = []  # ANCHOR Defign Before Function Is Actually Called
    while price == []:
        # print()
        price = getAmazonPrice(
            'https://www.amazon.in/dp/B087JWLZ2K/ref=s9_acsd_al_bw_c2_x_1_i?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-5&pf_rd_r=3FZHC0FVKBK77QYMJ0DQ&pf_rd_t=101&pf_rd_p=50675d9d-029a-42f0-8c73-fd7fe76f10f1&pf_rd_i=22817284031')
        v = list(price)
        # print('[+] Pinging')
        # print(price)
        # print(type(price))
        # print(v)
        # print(type(v))
    finalPrice = " ".join(v)
    finalPrice = finalPrice.strip()
    finalPrice = finalPrice.replace(" ", "")
    finalPrice = finalPrice.replace("₹", "")
    finalPrice = finalPrice.replace(",", "")
    finalPrice = float(finalPrice)

    currentPrice = finalPrice
    idealPrice = float(idealPrice)
    return currentPrice, idealPrice

# NOTE Main Function... Chicking The Chnage In Price


def priceChnageChecker(idealPrice, currentPrice):
    while idealPrice == currentPrice:
        getPriceUpdate(idealPrice)
    # ANCHOR ame Out Of WHile Loop => Price Changed
    if currentPrice > idealPrice:
        # ANCHORThe Message
        mssg = f'The Price Has Increased By {currentPrice - idealPrice}'
        # ANCHOR Sending A Email
        email = 'aviral270608@gmail.com'
        subject = 'Price Alert'
        mail = Mailer('aviral270608@gmail.com', 'A@2008viral')
        mail.send(receiver=email,
                  subject=subject, message=mssg)
        # ANCHOR Desktop Notification
        # notify2.init('Notification')
        # n = notify2.Notification(
        #     'Price Change', mssg)
        # n.show()

        status = False
    elif currentPrice < idealPrice:
        mssg = f'The Price Has Decreased By {idealPrice - currentPrice}'
        # ANCHOR Sending A Email
        email = 'aviral270608@gmail.com'
        subject = 'Price Alert'
        mail = Mailer('aviral270608@gmail.com', 'A@2008viral')
        mail.send(receiver=email,
                  subject=subject, message=mssg)
        # ANCHOR Desktop Notification
        # notify2.init('Notification')
        # n = notify2.Notification(
        #     'Price Change', mssg)
        # n.show()

        status = True
    return status


# NOTE 1st Time Run (Of Function) -- AFter That While Loops Run In Baground

try:
    idealPrice, currentPrice = getPriceUpdate(28999)
    priceChnageChecker(idealPrice, currentPrice)
except KeyboardInterrupt:
    print()
    print('[+] Exiting...')
    os.system('exit')
