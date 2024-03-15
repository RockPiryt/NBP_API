import requests

MY_LATITUDE = 54.352024
MY_LONGITUDE = 18.646639
API_KEY_OPEN_WEATHER = "keys"
OPEN_WEATHER_ENDPOINT ="https://api.openweathermap.org/data/2.5/weather"


parameters = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": API_KEY_OPEN_WEATHER,
}
response = requests.get(url=OPEN_WEATHER_ENDPOINT, params=parameters)
code = response.status_code
print(code)

data = response.json()
print(data)