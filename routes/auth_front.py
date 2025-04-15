import os
import requests
from flask import Blueprint, jsonify

AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL", "https://localhost:5173")
if not AUTH_SERVICE_URL.startswith(('http://', 'https://')):
    AUTH_SERVICE_URL = "http://" + AUTH_SERVICE_URL

authFront_bp = Blueprint('authFront', __name__)
    
@authFront_bp.route('/login', methods=['GET','POST'])
def login():
    try:
        response = requests.get(f"{AUTH_SERVICE_URL}/login")
        return response.content, response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
    
@authFront_bp.route('/register', methods=['GET','POST'])
def register():
    try:
        response = requests.get(f"{AUTH_SERVICE_URL}/register")
        return response.content, response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500