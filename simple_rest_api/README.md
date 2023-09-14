
---

# Simple REST API with CRUD Operations

## Overview

This project aims to develop a simple REST API capable of performing CRUD (Create, Read, Update, Delete) operations on a resource, in this case, a "person". The API is built using Python and Flask, and it interfaces with a MySQL database.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Endpoints](#endpoints)
4. [Sample Requests and Responses](#sample-requests-and-responses)
5. [Known Limitations and Assumptions](#known-limitations-and-assumptions)
6. [Setting Up and Deploying Locally](#setting-up-and-deploying-locally)
7. [Setting Up on a Server](#setting-up-on-a-server)

## Installation

To run this API locally, you'll need the following:

- Python 3.x installed on your system.
- MySQL server installed and running.

Next, install the required packages using pip:

```bash
pip install Flask Flask-SQLAlchemy
```

## Usage

1. Clone this repository to your local machine.
2. Set up your MySQL database with the necessary configurations.
3. Start the Flask application:

```bash
python app.py
```

The API will be accessible at `http://localhost:5000`.

## Endpoints

- **CREATE**: Adding a new person
  - Endpoint: `POST /api`
- **READ**: Fetching details of a person
  - Endpoint: `GET /api/<name>`
- **UPDATE**: Modifying details of an existing person
  - Endpoint: `PUT /api/<name>`
- **DELETE**: Removing a person
  - Endpoint: `DELETE /api/<name>`
- **Fetch All Persons** (Additional)
  - Endpoint: `GET /api/all`

## Sample Requests and Responses

### Create a New Person

**Request**:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "Mark Essein"}' http://localhost:5000/api
```

**Response**:

```json
{
  "message": "Person added successfully."
}
```

### Fetch Details of a Person

**Request**:

```bash
curl http://localhost:5000/api/John%20Doe
```

**Response**:

```json
{
  "id": 1,
  "name": "Mark Essein"
}
```

... (Continue with sample requests and responses for other operations)

## Known Limitations and Assumptions

- Only string names are allowed (no other data types).
- ...

Apologies for that. Let's continue:

---

## Known Limitations and Assumptions

- Only string names are allowed (no other data types).
- The API assumes a single user can be uniquely identified by their name.

## Setting Up and Deploying Locally

1. Ensure you have Python 3.x installed on your system.
2. Install the required packages using pip:

   ```bash
   pip install Flask Flask-SQLAlchemy
   ```

3. Set up your MySQL database with the necessary configurations.
4. Start the Flask application:

   ```bash
   python app.py
   ```

   The API will be accessible at `http://localhost:5000`.

## Setting Up on a Server

1. Deploy the Flask application on your preferred server. You can use platforms like Heroku, AWS, or any other hosting service.
2. Ensure that your server meets the necessary requirements (Python, MySQL, etc.).
3. Update the database configuration in the application to point to your server's MySQL instance.
4. Start the application on your server.

---
