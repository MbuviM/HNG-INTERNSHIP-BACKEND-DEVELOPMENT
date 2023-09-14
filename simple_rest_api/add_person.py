import requests

# Base URL of your API
base_url = 'http://localhost:5000/api'

# Send a POST request to add a person
response = requests.post(base_url, json={'name': 'Mark Essien', 'name': 'Melissa Nyokabi'})

# Print the response from the API
print(response.json())
