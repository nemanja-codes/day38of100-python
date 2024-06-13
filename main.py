import requests
from datetime import datetime

WEIGHT_KG = "88"
HEIGHT_CM = "190"
AGE = "25"

APP_ID = "cf4cf641"
API_KEY = "70e72e9ed023cbb55c90588e904bc068"

nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutri_config = {
    "query": input("Tell me which exercise you did: ")
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=nutri_endpoint, json=nutri_config, headers=headers)
response.raise_for_status()
result = response.json()
list_of_exercises = result["exercises"]

sheet_endpoint = "https://api.sheety.co/643dccdcddb0204a103d7f46ce9f9a94/workoutTracking/workouts"

now = datetime.now()
today_date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

for exercise in list_of_exercises:
    sheet_data_to_add = {
        "workout": {
            "date": today_date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": str(exercise["duration_min"]),
            "calories": str(exercise["nf_calories"])
        }
    }

    requests.post(url=sheet_endpoint, json=sheet_data_to_add)

