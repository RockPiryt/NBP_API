import requests
from datetime import datetime

MY_LATITUDE = 54.352024
MY_LONGITUDE = 18.646639

parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)

response.raise_for_status
code = response.status_code

data = response.json()["results"]

sunrise = response.json()["results"]["sunrise"].split("T")[1].split(":")[0]
print(sunrise)
sunset = response.json()["results"]["sunset"].split("T")[1].split(":")[0]
print(sunset)

time_now = datetime.now().hour
print(time_now)
