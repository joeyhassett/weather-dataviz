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



def create_photoscene():
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    data = {
    'scenename': 'testscene',
    'format': 'obj',
    'metadata_name[0]': 'targetcs',
    'scenetype': 'aerial',
    'metadata_value[0]': 'UTM84-32N',
    'gpstype':'precise',
    }

    response = requests.post('https://developer.api.autodesk.com/photo-to-3d/v1/photoscene', headers=headers, data=data)
    b = response.content
    return json.loads(b.decode("utf-8"))

photoscene_id = create_photoscene()["Photoscene"]["photosceneid"]

with open('photoscene_ids.txt', 'a') as f:
    print(photoscene_id, file=f)

def upload_images(start, end):

    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    files = {
        'photosceneid': (None, photoscene_id),
        'type': (None, 'image'),
    }

    for i in range(start, end):
         files[f'file[{i}]'] = open(f'images2/DJI_{str(i+1).zfill(4)}.jpg', 'rb')

    response = requests.post('https://developer.api.autodesk.com/photo-to-3d/v1/file', headers=headers, files=files)
    c = response.content
    return json.loads(c.decode("utf-8"))
print(upload_images(0, 20))
print(upload_images(20, 40))
print(upload_images(40, 60))
print(upload_images(60, 80))
print(upload_images(80, 100))
print(upload_images(100, 120))
print(upload_images(120, 140))
print(upload_images(140, 160))
print(upload_images(160, 180))
print(upload_images(180, 189))







def processing():
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    response = requests.post(f'https://developer.api.autodesk.com/photo-to-3d/v1/photoscene/{photoscene_id}', headers=headers)
    d = response.content
    return json.loads(d.decode("utf-8"))
processing()
