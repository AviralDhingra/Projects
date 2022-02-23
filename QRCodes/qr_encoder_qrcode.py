import inspect
import subprocess

import qrcode
import wifi_qrcode_generator

# class generator():
#     def __init__(self, type, content):
#         self.content = content
#         self.type = type


def link():
    img = qrcode.make("https://www.youtube.com/")  # Encode LInk
    img.save("img/youtubeQR.jpg")


def txt():
    img = qrcode.make(1234567890)  # Incode Text Data
    img.save("img/txt_data.jpg")


def wifi_login():
    try:
        # traverse the profile
        Id = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')

        id_results = str([b.split(":")[1][1:-1]
                          for b in Id if "Profile" in b])[2:-3]

        # traverse the password
        password = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'profiles',
             id_results, 'key=clear']).decode('utf-8').split('\n')

        pass_results = str([b.split(":")[1][1:-1]
                            for b in password if "Key Content" in b])[2:-2]
        print("User name :", id_results)
        print("Password :", pass_results)

    except:
        print(f'[-] Error !!\nTry Again...')
        wifi_login()

    # generate Qr code
    v = wifi_qrcode_generator.wifi_qrcode(
        id_results, False, 'WPA', pass_results)
    v.save("img/wifi_code.jpg")


def basic_wifi_login():
    # Use wifi_qrcode() to create a QR image
    v = wifi_qrcode_generator.wifi_qrcode(
        'Avi_5G ', False, 'WPA', 'kitneyaadmithay')
    print(v)
    v.save("img/wifi_code.jpg")
    # v.pack


# wifi_login()
# basic_wifi_login()
source_code_QrCodeGenerator = inspect.getsource(qrcode)
print(type(source_code_QrCodeGenerator))

# Write-Overwrites
file1 = open("source_code.txt", "w")  # write mode
file1.write(source_code_QrCodeGenerator + '\n')
file1.close()

# file1 = open("myfile.txt", "r")
# print "Output of Readlines after writing"
# print file1.readlines()
