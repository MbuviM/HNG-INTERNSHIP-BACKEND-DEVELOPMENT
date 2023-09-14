import requests

# Base URL of your API
base_url = 'http://localhost:5000/api'

# Send a POST request to add a person
# Send a POST request to add a person
response1 = requests.post(base_url, json={'name': 'Mark Essien'})
response2 = requests.post(base_url, json={'name': 'Melissa Nyokabi'})
response3 = requests.post(base_url, json={'name': 'Yvonne Mwende'})

# Print the responses
print(response1.json())
print(response2.json())
print(response3.json())