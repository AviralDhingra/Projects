import sys

import cv2

sys.argv = sys.argv


"""def input1():
    try:
        inp = sys.argv[1]
    except IndexError:
        inp = input('The Code You Want To Decode: ')
    # if inp.find('.jpg') != -1:
    #     pass
    # elif inp.find('.jpg') == -1:
    #     inp = inp + '.jpg'
    #     inp.strip
    # return inp"""

inp = sys.argv[1]
d = cv2.QRCodeDetector()
val, _, _ = d.detectAndDecode(cv2.imread(inp))
print("Decoded text is: ", val)

# txt_data.jpg
# youtubeQR.jpg
