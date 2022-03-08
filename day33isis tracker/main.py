from datetime import datetime
import requests

MY_LAT=51.5847351
MY_LONG=-0.127758 
'''
response=requests.get(url="http://api.open-notify.org/iss-now.json")

if response.status_code==404:
    raise Exception("That reponse does not exist.")
elif response.status_code==401:
    raise Exception("You are not authorised to access this data.")
'''
#response.raise_for_status()
#data=response.json()

#longitude = data["iss_position"]['longitude']
#latitude= data["iss_position"]["latitude"]

#iss_position={longitude,latitude}

#print(iss_position)
parameter={
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0
}

response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameter)
response.raise_for_status()
data=response.json()
sunrise=data["results"]["sunrise"]
sunset=data["results"]["sunset"]

print(sunrise)
time_now=datetime.now()

print(time_now.hour)




