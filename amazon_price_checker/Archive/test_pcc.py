import random

from priceChnageChecker import priceChnageChecker

print('Ideal Price Is 28999')
status = False
while status == False:
    v = random.randint(20000, 50000)
    print(f'The Random Number (Current Price) Is: {v}')
    # finalPrice = " ".join(v)  # v[0] + v[1] + v[2] ...
    # finalPrice = finalPrice.strip()
    # finalPrice = finalPrice.replace(" ", "")
    # finalPrice = finalPrice.replace("₹", "")
    # finalPrice = finalPrice.replace(",", "")
    finalPrice = float(v)

    status = priceChnageChecker(float(28999), finalPrice)
