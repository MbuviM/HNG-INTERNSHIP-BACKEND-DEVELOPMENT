from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)

# Configure the MySQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mwende:Mwende#2001!@localhost:3306/rest_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking

db = SQLAlchemy(app)

# Define the Person model
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

# Create the database and tables
with app.app_context():
    db.create_all()

# CREATE: Adding a new person
@app.route('/api', methods=['POST'])
def add_person():
    data = request.get_json()
    name = data.get('name')

    # Validation for name being a string
    if not isinstance(name, str):
        return jsonify({'error': 'Name must be a string.'}), 400
    
    person = Person(name=name)
    db.session.add(person)
    db.session.commit()

    return jsonify({'message': 'Person added successfully.'}), 201

# READ: Fetching details
@app.route('/api/<string:name>', methods=['GET'])
def get_person_by_name(name):
    person = Person.query.filter_by(name=name).first()
    if person is None:
        return jsonify({'error': 'Person not found.'}), 404
    return jsonify({'id': person.id, 'name': person.name}), 200

# UPDATE: Modify details of an existing person
@app.route('/api/<string:name>', methods=['PUT'])
def update_person_by_name(name):
    data = request.get_json()
    new_name = data.get('name')
    person = Person.query.filter_by(name=name).first()
    if person is None:
        return jsonify({'error': 'Person not found.'}), 404
    person.name = new_name
    db.session.commit()
    return jsonify({'message': 'Person updated successfully.'}), 200

# DELETE: Remove a person
@app.route('/api/<string:name>', methods=['DELETE'])
def delete_person_by_name(name):
    person = Person.query.filter_by(name=name).first()
    if person is None:
        return jsonify({'error': 'Person not found.'}), 404
    db.session.delete(person)
    db.session.commit()
    return jsonify({'message': 'Person deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)

