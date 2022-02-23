import os
import sys
import webbrowser

# import pyperclip

try:
    import pyperclip
except ModuleNotFoundError:
    os.system('pip install pyperclip')
    print()
    print('[+] PyperClip Is Installed')


sys.argv

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open(f'https://www.google.com/maps/place/{address}')
