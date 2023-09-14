
---

# Simple REST API Documentation

This document provides detailed information about the Simple REST API, including standard request/response formats, sample usage, known limitations, and instructions for setup and deployment.

## Standard Formats for Requests and Responses

### Create a New Person

**Request**:
- Method: POST
- Endpoint: `/api`
- Content-Type: application/json
- Body:
  ```json
  {
    "name": "John Doe"
  }
  ```

**Response**:
- Status: 201 Created
- Body:
  ```json
  {
    "message": "Person added successfully."
  }
  ```

### Fetch Details of a Person

**Request**:
- Method: GET
- Endpoint: `/api/<name>`

**Response**:
- Status: 200 OK
- Body:
  ```json
  {
    "id": 1,
    "name": "John Doe"
  }
  ```

... (Continue with request/response formats for other operations)

## Sample Usage of the API

### Create a New Person

**Request**:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe"}' http://localhost:5000/api
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
  "name": "John Doe"
}
```

... (Continue with sample requests and responses for other operations)

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
