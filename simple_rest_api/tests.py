import requests

# Base URL of your API
base_url = 'http://localhost:5000/api'

# Test CREATE operation
def test_create():
    response = requests.post(base_url, json={'name': 'Mark Essien'})
    print(response.json())

# Test READ operation
def test_read():
    response = requests.get(f'{base_url}/Mark%20Essien')
    print(response.json())


# Test UPDATE operation
def test_update():
    response = requests.put(f'{base_url}/Mark%20Essien', json={'name': 'Updated Name'})
    print(response.json())


# Test DELETE operation
def test_delete():
    response = requests.delete(f'{base_url}/1')
    print(response.json())

# Run the tests
test_create()
test_read()
test_update()
test_delete()
