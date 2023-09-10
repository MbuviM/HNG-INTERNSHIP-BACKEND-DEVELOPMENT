import datetime
from flask import Flask, request

api_app = Flask(__name__)

@api_app.route('/api', methods=['GET'])
def info_api():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Check if required parameters are missing
    if not slack_name or not track:
        return '{"status": 400, "message": "Missing required parameters"}', 400

    # Get current day and time in UTC
    current_day = datetime.datetime.utcnow().strftime('%A')
    utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # To calculate the time difference between the current UTC time and the request time
    request_time = datetime.datetime.utcnow()
    current_time = datetime.datetime.utcnow()
    time_difference = current_time - request_time

    if abs(time_difference.total_seconds()) > 120:
        return '{"status": 400, "message": "Invalid UTC time"}', 400

    # Construct the JSON response as a string
    response_data = (
        '{"slack_name": "%s", '
        '"current_day": "%s", '
        '"utc_time": "%s", '
        '"track": "%s", '
        '"github_file_url": "https://github.com/MbuviM/HNG-Internship-Backend-Development/blob/main/task0xAPI_Endpoint_Creation/API.py", '
        '"github_repo_url": "https://github.com/MbuviM/HNG-Internship-Backend-Development", '
        '"status_code": 200}'
    ) % (slack_name, current_day, utc_time, track)

    return response_data, 200, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    api_app.run(host='0.0.0.0', port=5000, debug=True)

