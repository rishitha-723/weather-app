import requests

API_KEY = "c8e38226a6d5cb87f8abf736af1f7104"

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(BASE_URL, params=params)

data = response.json()

if data["cod"] == 200:
    city_name   = data["name"]
    country     = data["sys"]["country"]
    temperature = data["main"]["temp"]
    feels_like  = data["main"]["feels_like"]
    humidity    = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    print("\n============================")
    print(f"  Weather in {city_name}, {country}")
    print("============================")
    print(f"  Temperature  : {temperature}°C")
    print(f"  Feels Like   : {feels_like}°C")
    print(f"  Humidity     : {humidity}%")
    print(f"  Condition    : {description.capitalize()}")
    print("============================\n")

else:
    print("City not found. Please check the spelling and try again.")