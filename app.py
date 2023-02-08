import requests
import datetime as dt





BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

API_KEY = "Your api key here"

CITY = "Add the city name here "

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

url = BASE_URL + "appid=" + API_KEY + "&q=" +CITY
response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)

feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)

wind_speed = response['wind']['speed']
humidity = response ['main'] ['humidity']
description = response['weather'][0]['description']
sunnrise_time = dt.datetime.utcfromtimestamp(response ['sys'] ['sunrise'] + response['timezone'])
sunnset_time = dt.datetime.utcfromtimestamp (response['sys'] ['sunset'] + response['timezone'])


print(f"Temperature  in {CITY}: {temp_celsius:.2f} °C or {temp_fahrenheit:.2f} °F")
print(f"Temperature  in {CITY} feels like: {feels_like_celsius:.2f} °C or {feels_like_fahrenheit} °F")

print(f"humidity  in {CITY}: {humidity}")
print(f"wind speed  in {CITY}: {wind_speed} m/s")
print(f"General weathetr in {CITY}: {description}")


print(f"sun rises in {CITY} at {sunnrise_time} local time")
print(f"sun sets in {CITY} at {sunnset_time} local time")
