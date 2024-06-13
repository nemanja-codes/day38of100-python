import requests

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
print(result)

