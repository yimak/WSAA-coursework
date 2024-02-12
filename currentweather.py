# import requests module
import requests
import json

# first install requests ---> python -m pip install requests
# https://www.geeksforgeeks.org/how-to-install-requests-in-python-for-windows-linux-mac/

response_API = requests.get('https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m')
 
# Making a get request
#reference: https://www.geeksforgeeks.org/response-json-python-requests/#:~:text=Convert%20Request%20Response%20to%20Dictionary%20in%20Python 
response = requests.get('https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m')
 
# Convert json into dictionary
response_dict = response.json()

# Pretty Printing JSON string back
# print(json.dumps(response_dict, indent=3, sort_keys=True))


# extract specific value from JSON response
#reference: https://www.tutorialspoint.com/python-program-to-extract-a-single-value-from-json-response#:~:text=Using%20APIs%20to%20Extract%20Values%20from%20a%20JSON%20Response
temperature = response_dict['current']['temperature_2m']

print(f'The actual temperature at 2 meters above ground is: {temperature} °C')


# We will follow the same logic the pull out the wind direction

response_API = requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m')

response = requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m')

response_dict1 = response.json()

wind_speed = response_dict1['current']['wind_speed_10m']

print(f'The actual temperature at 10 meters above ground is: {wind_speed} km/h')










