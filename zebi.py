# import requests module
import requests
import json
 
# Making a get request
#reference: https://www.geeksforgeeks.org/response-json-python-requests/#:~:text=Convert%20Request%20Response%20to%20Dictionary%20in%20Python 
response = requests.get('https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m')
 
# Convert json into dictionary
response_dict = response.json()

# Pretty Printing JSON string back
print(json.dumps(response_dict, indent=3, sort_keys=True))


# extract specific value from JSON response
#reference: https://www.tutorialspoint.com/python-program-to-extract-a-single-value-from-json-response#:~:text=Using%20APIs%20to%20Extract%20Values%20from%20a%20JSON%20Response
temperature = response_dict['current']['temperature_2m']

print(f'The temperature at 2 meters above the ground level is: {temperature}')