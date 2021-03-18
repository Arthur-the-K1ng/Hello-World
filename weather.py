import requests

api_key = "398d74b7f2ee475fba6141823211603"
base_url = "http://api.weatherapi.com/v1"
city = "Saint Petersburg"

parameters = {"key": api_key, "q": city}         # URL parameters
r = requests.get(f"{base_url}/current.json", params=parameters)

data = r.json()         # retrieve json

# retriving Data

location = data['location']['name']
time = data['location']['localtime']

condition = data['current']['condition']['text']
temperature_celcius = data['current']['temp_c']
temperature_farenheit = data['current']['temp_f']
feelslike_celcius = data['current']['feelslike_c']
wind_direction = data['current']['wind_dir']


# printing data
print(f"Location: {location}")
print(f"Current Time: {time}")
print()
print(f"Weather Condition: {condition}")
print(f"Temperature in Celcius: {temperature_celcius}")
print(f"Temperature in farenheit: {temperature_farenheit}")
print()
print(f"Temperature feels like: {feelslike_celcius} Celcius")
print(f"Wind Direction: {wind_direction}")
