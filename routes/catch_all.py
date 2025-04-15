import os
import requests
from flask import Blueprint, request, jsonify

# Use the same auth service URL as above
AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL", "http://auth-frontend:5173")
if not AUTH_SERVICE_URL.startswith(('http://', 'https://')):
    AUTH_SERVICE_URL = "http://" + AUTH_SERVICE_URL

catch_all_bp = Blueprint('catch_all', __name__)

@catch_all_bp.route('/', defaults={'path': ''})
@catch_all_bp.route('/<path:path>')
def catch_all(path):
    try:
        # Forward the request to the auth-frontend service
        response = requests.get(f"{AUTH_SERVICE_URL}/{path}")
        return response.content, response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500