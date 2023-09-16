from flask import Flask, request, jsonify
from supabase import create_client

# Initialize Flask application
app = Flask(__name__)

# Configure the Supabase database connection
supabase_url = "https://cicqhphudmrtycypnqnw.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNpY3FocGh1ZG1ydHljeXBucW53Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTQ4MzQyNjMsImV4cCI6MjAxMDQxMDI2M30.rbvtSz4nxT7V-DPo718TB3G9EnIm7zZibRrOcpq-Pi8"
supabase = create_client(supabase_url, supabase_key)

# Define the Person model (optional, you can use Supabase tables directly)
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# CREATE: Adding a new person
@app.route('/api', methods=['POST'])
def add_person():
    data = request.get_json()
    name = data.get('name')

    # Validation for name being a string
    if not isinstance(name, str):
        return jsonify({'error': 'Name must be a string.'}), 400

    response = supabase.table('your_table_name').insert([{'name': name}])
    
    if response['status_code'] == 201:
        return jsonify({'message': 'Person added successfully.'}), 201
    else:
        return jsonify({'error': 'Failed to add person.'}), 500

# READ: Fetching details
@app.route('/api/<string:name>', methods=['GET'])
def get_person_by_name(name):
    response = supabase.table('your_table_name').select().eq('name', name)
    person_data = response['data']

    if person_data:
        person = Person(person_data[0]['id'], person_data[0]['name'])
        return jsonify({'id': person.id, 'name': person.name}), 200
    else:
        return jsonify({'error': 'Person not found.'}), 404

# UPDATE: Modify details of an existing person
@app.route('/api/<string:name>', methods=['PUT'])
def update_person_by_name(name):
    data = request.get_json()
    new_name = data.get('name')

    response = supabase.table('your_table_name').select().eq('name', name)
    person_data = response['data']

    if not person_data:
        return jsonify({'error': 'Person not found.'}), 404
    
    person = person_data[0]
    person['name'] = new_name

    response = supabase.table('your_table_name').upsert([person])
    
    if response['status_code'] == 200:
        return jsonify({'message': 'Person updated successfully.'}), 200
    else:
        return jsonify({'error': 'Failed to update person.'}), 500

# DELETE: Remove a person
@app.route('/api/<string:name>', methods=['DELETE'])
def delete_person_by_name(name):
    response = supabase.table('rest_api').delete().eq('name', name)
    
    if response['status_code'] == 200:
        return jsonify({'message': 'Person deleted successfully.'}), 200
    else:
        return jsonify({'error': 'Failed to delete person.'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
