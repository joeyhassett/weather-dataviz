# Import google_streetview for the api module
import google_streetview.api

adict = {}
for i in range(20):
    # Define parameters for street view api
    params = [{
        'size': '600x300', # max 640x640 pixels
        'location': '33.7736,-84.4022',
        'heading': f'{i*36}' ,
        'pitch': '-0.76',
        'key': 'AIzaSyB8atCJJPW1nddKKHS4XWwuHKRaHbJ-llU'
    }]

    # Create a results object
    adict[i] = google_streetview.api.results(params)

print(adict)

# Download images to directory 'downloads'
for key in adict.keys():
    adict[key].download_links(f'downloads_{key}')