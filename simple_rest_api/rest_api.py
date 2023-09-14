from flask import Flask, request, jsonify

# Initialize Flask application
rest_api = Flask(__name__)

# List that acts as a database
persons = []

# Define endpoints for CRUD operations

# CREATE: Adding a new person
@rest_api.route('/api', methods=['POST'])
def add_person():
    data = request.get_json()
    name = data.get('name')

    # Validation for name being a string
    if not isinstance(name, str):
        return jsonify({'error': 'Name must be a string.'}), 400
    
    person = {'name': name}
    persons.append(person)
    return jsonify({'message': 'Person added successfully.'}), 201

@rest_api.route('/api/<string:name>', methods=['GET'])
def get_person_by_name(name):
    person = next((p for p in persons if p['name'] == name), None)
    if person is None:
        return jsonify({'error': 'Person not found.'}), 404
    return jsonify(person), 200

@rest_api.route('/api/<string:name>', methods=['PUT'])
def update_person_by_name(name):
    data = request.get_json()
    new_name = data.get('name')
    person = next((p for p in persons if p['name'] == name), None)
    if person is None:
        return jsonify({'error': 'Person not found.'}), 404
    person['name'] = new_name
    return jsonify({'message': 'Person updated successfully.'}), 200

@rest_api.route('/api/<string:name>', methods=['DELETE'])
def delete_person_by_name(name):
    global persons
    persons = [p for p in persons if p['name'] != name]
    return jsonify({'message': 'Person deleted successfully'}), 200
