import google_streetview.api

# Open the file to read the coordinates
location = open('coor', "r");
lon = location.readline()
lat = location.readline()
location.close()

# Define parameters for street view api
params = [{
  'size': '600x300', # max 640x640 pixels
  'location': f'{lon}, {lat}',
  'heading': f'{i*9}' ,
  'pitch': '-0.76',
  'key': 'AIzaSyB8atCJJPW1nddKKHS4XWwuHKRaHbJ-llU'
} for i in range(100)]

# Create a results object
result = google_streetview.api.results(params)

# Download images to directory 'downloads'
result.download_links('streetview_images')
