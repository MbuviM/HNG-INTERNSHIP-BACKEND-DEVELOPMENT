import datetime
#  Setting up Flask
from flask import Flask, request, jsonify

api_app = Flask(__name__)

# Creating the API endpoint
# Decorator
@api_app.route('/hng_info', methods=['GET']) #'/hng_info' is the path
def info_api():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    current_day = datetime.datetime.utcnow().strftime('%A') # Give day in full
    utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ') # Gives time in UTC format
    # To calculate the time difference between the current UTC time and the request time
    request_time = datetime.datetime.strptime(request.headers['Date'], '%a, %d %b %Y %H:%M:%S %Z')
    time_difference = datetime.datetime.utcnow() - request_time

    if abs(time_difference.total_seconds()) > 120:
        return jsonify({"status": "error", "message": "Invalid UTC time"}), 400

    #JSON Response
    response_data = {
    "slack_name": slack_name,
    "current_day": current_day,
    "utc_time": utc_time,
    "track": track,
    "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
    "github_repo_url": "https://github.com/MbuviM/HNG-Internship-Backend-Development.git",
    "status_code": 200
    }












