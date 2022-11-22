import requests
import keys
from twilio.rest import Client

# PROVIDING WEATHER DATA PARAMETERS
parameters = {
    "lat": keys.latitude,
    "lon": keys.longitude,
    "appid": keys.api_key,
    "exclude": "current,minutely,daily"
}

# ----------------------------------------------------------------------------------------------------

# RETRIEVING DATA FROM THE WEATHER API
request = requests.get(
    "https://api.openweathermap.org/data/3.0/onecall", params=parameters)
data = request.json()["hourly"][:12]

# ----------------------------------------------------------------------------------------------------

# CHECKING IF IT WILL RAIN WITHIN THE FIRST 12 HOURS
condition_code = [hour["weather"][0]["id"]
                  for hour in data if int(hour["weather"][0]["id"]) < 700]

# -----------------------------------------------------------------------------------------------------

# COMPLETING REQUEST TO TWILIO API

client = Client(keys.account_sid, keys.auth_token)

if condition_code:
    message = client.messages \
                    .create(
                        body="Bring An Umberella. Looks like it is going to rain today",
                        from_=keys.sender,
                        to=keys.receiver
                    )
