import requests
from pprint import pprint

## getting lat/long from address through api call
address = "750 Ferst Dr, Atlanta, GA 30318" # needs to be full address; partials don't work
loc_apikey = "aOgwwD7ajrzcnfTx3pJKPfpjL0HvSgzA"
url_loc = f"https://api.tomtom.com/search/2/geocode/{address}.json?key={loc_apikey}"
loc = requests.get(url_loc)
loc = loc.json()


## getting weather info through api call
weather_apikey = "ffca7caa3de044cc81aba3bd77db4636"
lat = loc["results"][0]["entryPoints"][0]["position"]["lat"]
lon = loc["results"][0]["entryPoints"][0]["position"]["lon"]
url_weather = f"https://api.weatherbit.io/v2.0/forecast/daily?lat={lat}&lon={lon}&key={weather_apikey}"
weather = requests.get(url_weather)
weather = weather.json()

## printing weather and wind to dictionary
weather_dict = {}
for day in range(16):
    if day == 0:
        weather_dict[f"Today:"] = [weather["data"][day]["weather"]["description"], weather["data"][day]["wind_spd"]]
    elif day == 1:
        weather_dict[f"Tomorrow:"] = [weather["data"][day]["weather"]["description"], weather["data"][day]["wind_spd"]]
    else:
        weather_dict[f"{day} days out:"] = [weather["data"][day]["weather"]["description"], weather["data"][day]["wind_spd"]]

## organizing different weather categories into groups for ease of environment creation
thunderstorms = ["Thunderstorm with light rain", "Thunderstorm with rain", "Thunderstorm with heavy rain", "Thunderstorm with light drizzle", "Thunderstorm with drizzle", "Thunderstorm with heavy drizzle", "Thunderstorm with hail"]
drizzles = ["Light drizzle", "Drizzle", "Heavy drizzle"]
rains = ["Light rain", "Moderate rain", "Heavy rain", "Freezing rain", "Light shower rain", "Shower rain", "Heavy shower rain", "Unknown Precipitation"]
snows = ["Light snow", "Snow", "Heavy Snow", "Mix snow/rain", "Sleet", "Snow shower", "Heavy snow shower", "Flurries"]
clouds = ["Mist", "Smoke", "Haze", "Sand/dust", "Fog", "Freezing Fog", "Few clouds", "Scattered clouds", "Broken clouds", "Overcast clouds"]

## resetting values for weather categories
for key in weather_dict.keys():
    if weather_dict[key][0] in thunderstorms:
        weather_dict[key][0] = "Thunderstorm"
    elif weather_dict[key][0] in drizzles:
        weather_dict[key][0] = "Drizzle"
    elif weather_dict[key][0] in rains:
        weather_dict[key][0] = "Rain"
    elif weather_dict[key][0] in snows:
        weather_dict[key][0] = "Snow"
    elif weather_dict[key][0] in clouds:
        weather_dict[key][0] = "Cloudy"
    else:
        weather_dict[key][0] = "Clear skies"

## resetting values for windiness (0/1; binary)
for key in weather_dict.keys():
    if weather_dict[key][1] >= 4:
        weather_dict[key][1] = 1 # 1 signifies windy
    else:
        weather_dict[key][1] = 0 # 0 signifies not windy

## LAST STEP - FILE IO
with open("weatherdata.csv", "w") as outfile:
    outfile.write("Day, Weather, Windy")
    for key, value in weather_dict.items():
        day = key.strip(":")
        weather = value[0]
        windy = value[1]
        outfile.write(f"\n{day}, {weather}, {windy}")