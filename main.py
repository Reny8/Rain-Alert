import requests
import keys
import json
parameters = {
    "lat": keys.latitude,
    "lon": keys.longitude,
    "appid": keys.api_key,
    "exclude": "current,minutely,daily"
}
# RETRIEVING DATA
request = requests.get(
    "https://api.openweathermap.org/data/3.0/onecall", params=parameters)
data = request.json()["hourly"][:12]

# CHECKING IF IT WILL RAIN WITHIN THE FIRST 12 HOURS
condition_code = [hour["weather"][0]["id"]
                  for hour in data if int(hour["weather"][0]["id"]) < 700]
if condition_code:
    print("Bring an umberella")

