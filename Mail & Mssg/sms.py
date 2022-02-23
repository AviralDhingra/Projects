import requests

url = "https://www.fast2sms.com/dev/bulk"


# payload = "sender_id=FSTSMS&message=test&language=english&route=p&numbers=9999999999,888888888"

payload = "sender_id=FSTSMS&message=Good Morning&language=english&route=p&numbers=9999937141,854112799"


headers = {
    'authorization': "n2WAIrLcpqhf8Gjy9xSdkYb5Fua3BUz61DHwMsXCvgKNEtoZPRJSOGo8xL5ymBnKUzHXMVZeN0kTf2jD",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
