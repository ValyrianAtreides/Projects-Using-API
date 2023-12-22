import requests
from datetime import datetime
import os

APP_ID=os.environ.get("APP_ID")
API_KEY=os.environ.get("API_KEY")
SHEET_ENDPOINT=os.environ.get("SHEET_ENDPOINT")
BASIC_TOKEN=os.environ.get("BASIC_TOKEN")

user_answer=input("What did you do today?")

nutrionix_endpoint="https://trackapi.nutritionix.com/v2/natural/exercise"

nutrionix_headers={
    "x-app-id":APP_ID,
    "x-app-key":API_KEY
}

data={
    "query":user_answer
}

response = requests.post(url=nutrionix_endpoint, headers=nutrionix_headers, json=data)

exercise_data=response.json()
for exercise in exercise_data["exercises"]:
    exercise_name = exercise["user_input"]
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]



sheety_header = {
    "Authorization": f"Basic {BASIC_TOKEN} ",
    "Content-Type": "application/json"
}
now=datetime.now()

sheety_data = {
    "workout": {
        "date": now.strftime("%d%m%Y"),
        "time": now.strftime("%H:%M:%S"),
        "exercise": exercise_name,
        "duration": duration,
        "calories": calories
    }
}

sheety_response = requests.post(url=SHEET_ENDPOINT, headers=sheety_header, json=sheety_data)
