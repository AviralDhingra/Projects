# import inspect
# import subprocess

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


# def wifi_login_advanced():
#     try:
#         # traverse the profile
#         Id = subprocess.check_output(
#             ['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')

#         id_results = str([b.split(":")[1][1:-1]
#                           for b in Id if "Profile" in b])[2:-3]

#         # traverse the password
#         password = subprocess.check_output(
#             ['netsh', 'wlan', 'show', 'profiles',
#              id_results, 'key=clear']).decode('utf-8').split('\n')

#         pass_results = str([b.split(":")[1][1:-1]
#                             for b in password if "Key Content" in b])[2:-2]
#         print("User name :", id_results)
#         print("Password :", pass_results)

#     except:
#         print(f'[-] Error !!\nTry Again...')
#         wifi_login_advanced()

#     v = wifi_qrcode_generator.wifi_qrcode(
#         id_results, False, 'WPA2', pass_results)
#     v.save("img/wifi_code.jpg")


def basic_wifi_login(ussid, security_type, password):
    v = wifi_qrcode_generator.wifi_qrcode(
        ussid, False, security_type, password)
    print(v)
    v.save("img/wifi_code.jpg")
    # v.pack
