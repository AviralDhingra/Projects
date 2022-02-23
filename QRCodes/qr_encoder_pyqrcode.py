# Import QRCode from pyqrcode
import sys

# import png
import pyqrcode
from pyqrcode import QRCode

# String which represents the QR code
s = sys.argv[1]

# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file naming "myqr.svg"
url.svg("img/myqr.svg", scale=8)

# Create and save the png file naming "myqr.png"
url.png('img/myqr.png', scale=6)
