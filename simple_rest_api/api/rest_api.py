from flask import Flask, request, jsonify
from supabase import create_client

import os
from dotenv import load_dotenv
load_dotenv()

# Initialize Flask application
app = Flask(__name__)

# Configure the Supabase database connection
#your creds
supabase_url = "https://cicqhphudmrtycypnqnw.supabase.co"
#use the secret key to bypass row-level restriction instead of public key
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNpY3FocGh1ZG1ydHljeXBucW53Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTQ4MzQyNjMsImV4cCI6MjAxMDQxMDI2M30.rbvtSz4nxT7V-DPo718TB3G9EnIm7zZibRrOcpq-Pi8"

#my creds (environment variables) using.env
supabase_key=os.getenv('SUPABASE_KEY')
supabase_url=os.getenv('SUPABASE_URL')
supabase = create_client(supabase_url, supabase_key)
@app.route('/')
def index():
    return 'Hello world!'

# CREATE: Adding a new person
#all response objects from supabase dont contain a status code
@app.route('/api', methods=['POST'])
def add_person():
    data = request.get_json()
    name = data.get('name')

    # Validation for name being a string
    if not isinstance(name, str):
        return jsonify({'error': 'Name must be a string.'}), 400

    response = supabase.table('rest_api').insert({'name': name}).execute()
    
    if response.data:
        return {'message': 'Person added successfully.'}, 201
    else:
        return jsonify({'error': 'Failed to add person.'}), 500
   

    

# READ: Fetching details
@app.route('/api/<string:name>', methods=['GET'])
def get_person_by_name(name):
    response = supabase.table('rest_api').select('*').eq('name', name).execute()
    person_data = response.data

    if person_data:
        return jsonify(person_data), 200
    else:
        return jsonify({'error': 'Person not found.'}), 404

# UPDATE: Modify details of an existing person
@app.route('/api/<string:name>', methods=['PUT'])
def update_person_by_name(name):
    data = request.get_json()
    new_name = data.get('name')
    #check if the name is in the table
    response = supabase.table('rest_api').select('name').eq('name',name).execute()
    person_data = response.data
   
    if not person_data:
        return jsonify({'error': 'Person not found.'}), 404
    
    person = person_data[0]
    person['name'] = new_name

    # response = supabase.table('rest_api').upsert([person])
    #update only if the name is found
    #update ->set {new_name} in rest_api where name column is equal to the {name} passed 
    response = supabase.table('rest_api').update({'name':new_name}).eq('name',name).execute()
    to_updated_person_data = response.data

    if  to_updated_person_data:
        return jsonify({'message': 'Person updated successfully.'}), 200
    else:
        return jsonify({'error': 'Failed to update person.'}), 500

# DELETE: Remove a person
@app.route('/api/<string:name>', methods=['DELETE'])
def delete_person_by_name(name):
    response = supabase.table('rest_api').delete().eq('name', name).execute()
    
    if response.data:
        return jsonify({'message': 'Person deleted successfully.'}), 200
    else:
        return jsonify({'error': 'Failed to delete person.'}), 500
    
# GETTING ALL USERS

@app.route('/api/all', methods=['GET'])
def get_all_persons():
    response = supabase.table('rest_api').select('*').execute()
    persons_data = response.data

    if persons_data:
        return jsonify(persons_data), 200
    else:
        return jsonify({'message': 'No records found.'}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)