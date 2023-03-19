from pprint import pprint
import requests
import json

url = "https://api.mindbox.ru/v3/operations/sync?endpointId=hiring&operation=get.user"
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Accept": "application/json",
    "Authorization": "Mindbox secretKey=\"QQ5oyl5DLBhKeLrQO1A2\""
}
body = {
    "customer": {"email": "demo@mindbox.cloud"}
}

response = requests.post(url, headers=headers, json=body)
pprint(response.json())