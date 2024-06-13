import requests
from datetime import datetime
import os

WEIGHT_KG = "88"
HEIGHT_CM = "190"
AGE = "25"

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("APP_KEY")
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")

nutri_endpoint = os.environ.get("NUTRI_ENDPOINT")

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

sheet_header = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

response = requests.post(url=nutri_endpoint, json=nutri_config, headers=headers)
response.raise_for_status()
result = response.json()
list_of_exercises = result["exercises"]

sheet_endpoint = os.environ.get("SHEET_ENDPOINT")

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

    requests.post(url=sheet_endpoint, json=sheet_data_to_add, headers=sheet_header)

