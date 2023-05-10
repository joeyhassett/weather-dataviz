import requests
import json
import base64

client_id = 'ocuHHvZRM6AxCSNFBdk5yYkmA7AA48CQ'
client_secret = 'R19ae02039c114ad'
auth = base64.b64encode(bytes(f"{client_id}:{client_secret}", encoding='ascii')).decode()
#b2N1SEh2WlJNNkF4Q1NORkJkazV5WWttQTdBQTQ4Q1E6UjE5YWUwMjAzOWMxMTRhZA==

def get_token():
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'Authorization': f'Basic {auth}',
    }

    data = {
    'grant_type': 'client_credentials',
    'scope': 'data:write data:read'
    }

    response = requests.post('https://developer.api.autodesk.com/authentication/v2/token', headers=headers, data=data)
    a = response.content
    return json.loads(a.decode("utf-8"))
token_response = get_token()
access_token = token_response["access_token"]

with open("photoscene_ids.txt") as f:
    photoscene_id = f.readlines()[-1]
    photoscene_id = photoscene_id.strip()

def progress_poll():
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    response = requests.get(f'https://developer.api.autodesk.com/photo-to-3d/v1/photoscene/{photoscene_id}/progress', headers=headers)
    e = response.content
    return json.loads(e.decode("utf-8"))

while True:
    msg = progress_poll()
    progress_msg = msg["Photoscene"]["progressmsg"]
    progress_percentage = int(msg["Photoscene"]["progress"])
    if progress_percentage != 0:
        print(msg)
    if progress_msg == "DONE" or progress_percentage == 100:
        break



def download_result():

    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    params = {
        'format': 'obj',
    }

    response = requests.get(f'https://developer.api.autodesk.com/photo-to-3d/v1/photoscene/{photoscene_id}', headers=headers, params=params)
    f = response.content
    print(f)
    return json.loads(f.decode("utf-8"))
download_result()