import requests

## Base URL of your API
base_url = 'https://cicqhphudmrtycypnqnw.supabase.co/rest/v1/rest_api'

# Add your Supabase API key here
api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNpY3FocGh1ZG1ydHljeXBucW53Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTQ4MzQyNjMsImV4cCI6MjAxMDQxMDI2M30.rbvtSz4nxT7V-DPo718TB3G9EnIm7zZibRrOcpq-Pi8'

# Define headers with the API key
headers = {
    'Content-Type': 'application/json',
    'apikey': api_key,
}

# Test CREATE operation
def test_create():
    response = requests.post(base_url, json={'name': 'Yvonne Mwende'})
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: {response.status_code}")

# Test READ operation
def test_read():
    response = requests.get(f'{base_url}?name=eq.Yvonne Mwende')
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: {response.status_code}")

# Test UPDATE operation
def test_update():
    response = requests.patch(base_url, json=[{'name': 'Updated Name'}])
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: {response.status_code}")

# Test DELETE operation
def test_delete():
    response = requests.delete(f'{base_url}?name=eq.Yvonne Mwende')
    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Error: {response.status_code}")

# Run the tests
test_create()
test_read()
test_update()
test_delete()
