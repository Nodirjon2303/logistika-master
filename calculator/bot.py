import requests
url = "https://api.telegram.org/bot5208426778%3AAAEQomXaq0bfk2PaYRLaNjxmDrU8_D0weBw/sendMessage"

payload = {
    "text": "Dalbayof gandoncha",
    "chat_id": '2133918786'
}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)