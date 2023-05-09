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
    'format': 'obj,ortho',
    # 'metadata_name[0]': 'targetcs',
    # 'metadata_value[0]': 'UTM84-32N',
    'scope': 'user-profile:read'
    }

    response = requests.post('https://developer.api.autodesk.com/photo-to-3d/v1/photoscene', headers=headers, data=data)
    b = response.content
    return json.loads(b.decode("utf-8"))

photoscene_id = create_photoscene()["Photoscene"]["photosceneid"]

def upload_images():

    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    files = {
        'photosceneid': (None, photoscene_id),
        'type': (None, 'image'),
        'file[0]': 'https://gitlab.com/photogrammetry-test-sets/dice-turntable-strong-lights-heavily-textured-w-watercolors/-/raw/master/01.JPG',
        'file[1]': 'https://gitlab.com/photogrammetry-test-sets/dice-turntable-strong-lights-heavily-textured-w-watercolors/-/raw/master/02.JPG',
        'file[2]': 'https://gitlab.com/photogrammetry-test-sets/dice-turntable-strong-lights-heavily-textured-w-watercolors/-/raw/master/06.JPG',
        'file[3]': 'https://gitlab.com/photogrammetry-test-sets/dice-turntable-strong-lights-heavily-textured-w-watercolors/-/raw/master/09.JPG',
        'file[4]': 'https://gitlab.com/photogrammetry-test-sets/dice-turntable-strong-lights-heavily-textured-w-watercolors/-/raw/master/11.JPG',
        'file[5]': 'https://gitlab.com/photogrammetry-test-sets/dice-turntable-strong-lights-heavily-textured-w-watercolors/-/raw/master/13.JPG'
    }

    # for i in range(60):
    #     files[f'file[{i}]'] = open(f'streetview_images/gsv_{i}.jpg', 'rb')

    response = requests.post('https://developer.api.autodesk.com/photo-to-3d/v1/file', headers=headers, files=files)
    c = response.content
    return json.loads(c.decode("utf-8"))
upload_images()

def processing():
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    response = requests.post(f'https://developer.api.autodesk.com/photo-to-3d/v1/photoscene/{photoscene_id}', headers=headers)
    d = response.content
    return json.loads(d.decode("utf-8"))
processing()

def progress_poll():
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    response = requests.get(f'https://developer.api.autodesk.com/photo-to-3d/v1/photoscene/{photoscene_id}/progress', headers=headers)
    e = response.content
    print(e)
    return json.loads(e.decode("utf-8"))
progress_poll()

def download_result():

    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    params = (
        ('format', 'rcm'),
    )

    response = requests.get(f'https://developer.api.autodesk.com/photo-to-3d/v1/photoscene/{photoscene_id}', headers=headers, params=params)
    f = response.content
    print(f)
    return json.loads(f.decode("utf-8"))
download_result()