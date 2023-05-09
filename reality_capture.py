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
    'scope': 'data:write'
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
    'format': 'obj,ortho',
    'metadata_name[0]': 'targetcs',
    'metadata_value[0]': 'UTM84-32N',
    'scope': 'user-profile:read'
    }

    response = requests.post('https://developer.api.autodesk.com/photo-to-3d/v1/photoscene', headers=headers, data=data)
    print(response.content)
create_photoscene()
