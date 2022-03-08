import requests
from twilio.rest import Client

owm_endpoint="https://api.openweathermap.org/data/2.5/onecall"
api_key="32bafd6fd4038931ddc44acf9fbadd6d"

weather_params={
    "lat":23.404230,
    "lon":85.394440,
    "appid":api_key
}
response=requests.get(owm_endpoint,params=weather_params)
print(response.json())
