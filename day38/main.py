import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 72
HEIGHT_CM = 179
AGE = 19

APP_ID = "d82dc1e7"
API_KEY = "1b401e89e4fa6589ebf4daba9fe76ca3"


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = YOUR SHEETY ENDPOINT

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

################### Start of Step 4 Solution ######################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)

#No Authentication  
sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
  
#Basic Authentication
sheet_response = requests.post(
  sheet_endpoint, 
  json=sheet_inputs, 
  auth=(
      YOUR USERNAME, 
      YOUR PASSWORD,
  )
)

#Bearer Token Authentication
bearer_headers = {
"Authorization": "Bearer YOUR_TOKEN"
}
sheet_response = requests.post(
    sheet_endpoint, 
    json=sheet_inputs, 
    headers=bearer_headers
)